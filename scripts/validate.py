#!/usr/bin/env python3
"""Check data/videos.json, prompts/, README.md, and the link snapshot.

Default mode is offline. ``--links`` rechecks URLs and rewrites
data/link-check.json.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "videos.json"
README = ROOT / "README.md"
LINKS = ROOT / "data" / "link-check.json"
PROMPTS = ROOT / "prompts"

REQUIRED_GALLERY = {
    "id",
    "slug",
    "author",
    "author_url",
    "post_url",
    "in_seed",
    "surfaced_via",
    "category",
    "title",
    "summary",
    "created_at",
    "attribution",
    "independently_reproduced",
    "comparison_with",
    "tech",
    "prompt",
    "prompt_partial",
    "prompt_note",
    "prompt_file",
    "preview_url",
    "preview_frame_reviewed",
    "media",
    "caveats",
    "text",
    "metrics",
}
CATEGORIES = {"3d", "character", "comparison"}
CATEGORY_LABELS = {
    "3d": "Three.js 與 3D 場景",
    "character": "角色、動態與繪像",
    "comparison": "對照",
}
SH = timezone(timedelta(hours=8))


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def load() -> dict:
    return json.loads(DATA.read_text(encoding="utf-8"))


def prompt_body(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"```text\n(.*)\n```", text, re.S)
    if not match:
        raise ValueError(f"{path} has no ```text fence")
    return match.group(1)


def check_record_url(errors: list[str], item: dict, where: str) -> None:
    author = item["author"]
    post_id = item["id"]
    expected = f"https://x.com/{author}/status/{post_id}"
    if item.get("post_url") != expected:
        fail(errors, f"{where} {post_id} post_url {item.get('post_url')!r} != {expected}")
    if item.get("author_url") != f"https://x.com/{author}":
        fail(errors, f"{where} {post_id} author_url mismatch")
    created = item.get("created_at") or ""
    if not created.endswith("Asia/Shanghai(UTC+8)"):
        fail(errors, f"{where} {post_id} timestamp is not Asia/Shanghai")


def check(data: dict) -> list[str]:
    errors: list[str] = []
    meta = data["meta"]
    gallery = data["gallery"]
    context = data["context"]
    excluded = data["excluded"]

    if meta.get("official_release_confirmed") is not False:
        fail(errors, "official_release_confirmed must stay false")
    if meta.get("model_status") != "unconfirmed_community_name":
        fail(errors, "model_status mismatch")

    ids = [item["id"] for item in gallery + context + excluded]
    if len(ids) != len(set(ids)):
        dupes = [i for i, n in Counter(ids).items() if n > 1]
        fail(errors, f"duplicate ids: {dupes}")
    slugs = [item["slug"] for item in gallery]
    if len(slugs) != len(set(slugs)):
        fail(errors, "duplicate gallery slugs")

    in_seed = [item for item in gallery if item["in_seed"]]
    resolved = [item for item in gallery if not item["in_seed"]]
    seed_rows = in_seed + context + excluded
    if len(seed_rows) != meta["seed_post_count"]:
        fail(errors, f"seed coverage {len(seed_rows)} != {meta['seed_post_count']}")
    if len(gallery) != meta["gallery_count"]:
        fail(errors, "gallery_count mismatch")
    if len(in_seed) != meta["gallery_in_seed_count"]:
        fail(errors, "gallery_in_seed_count mismatch")
    if len(resolved) != meta["gallery_resolved_original_count"]:
        fail(errors, "gallery_resolved_original_count mismatch")
    if len(context) != meta["context_count"]:
        fail(errors, "context_count mismatch")
    if len(excluded) != meta["excluded_count"]:
        fail(errors, "excluded_count mismatch")

    by_cat = Counter(item["category"] for item in gallery)
    for key, label in CATEGORY_LABELS.items():
        if by_cat[key] != meta["category_counts"][key]:
            fail(errors, f"category {key} count mismatch")
        if meta["category_labels"][key] != label:
            fail(errors, f"category label {key} mismatch")

    prompt_items = [item for item in gallery if item["prompt"] is not None]
    partial = [item for item in prompt_items if item["prompt_partial"]]
    if len(prompt_items) != meta["prompt_file_count"]:
        fail(errors, "prompt_file_count mismatch")
    if len(partial) != meta["prompt_partial_count"]:
        fail(errors, "prompt_partial_count mismatch")

    raw = json.dumps(data, ensure_ascii=False)
    if "skillry" in raw.lower() or "video.twimg.com" in raw or ".mp4" in raw:
        fail(errors, "json contains a remake host or a full video file url")

    files_on_disk = sorted(p.name for p in PROMPTS.glob("*.md"))
    expected_files = sorted(Path(item["prompt_file"]).name for item in prompt_items)
    if files_on_disk != expected_files:
        fail(errors, f"prompt files {files_on_disk} != records {expected_files}")

    for item in gallery:
        missing = REQUIRED_GALLERY - item.keys()
        if missing:
            fail(errors, f"{item.get('id')} missing {sorted(missing)}")
            continue
        check_record_url(errors, item, "gallery")
        if item["category"] not in CATEGORIES:
            fail(errors, f"{item['id']} bad category")
        if item["attribution"] != "creator_reported" or item["independently_reproduced"] is not False:
            fail(errors, f"{item['id']} attribution flags are wrong")
        if item["category"] == "comparison" and not item["comparison_with"]:
            fail(errors, f"{item['id']} comparison has no comparison_with")
        if not item["preview_url"].startswith("https://pbs.twimg.com/"):
            fail(errors, f"{item['id']} preview is not a public twimg url")
        if item["prompt"] is None:
            if item["prompt_file"] is not None or item["prompt_partial"] is not False:
                fail(errors, f"{item['id']} null prompt still has a file or partial flag")
        else:
            if item["prompt_file"] != f"prompts/{item['slug']}.md":
                fail(errors, f"{item['id']} prompt_file path")
            body = prompt_body(PROMPTS / f"{item['slug']}.md")
            if body != item["prompt"]:
                fail(errors, f"{item['id']} prompt file does not match json")
            if item["prompt"] not in item["text"]:
                fail(errors, f"{item['id']} prompt is not an exact substring of the post")
        if not item["in_seed"]:
            via = item["surfaced_via"] or {}
            if not via.get("id") or not via.get("url"):
                fail(errors, f"{item['id']} resolved original lacks surfaced_via")
        if "Asia/Shanghai" not in item["created_at"]:
            fail(errors, f"{item['id']} created_at")

    for bucket, name in ((context, "context"), (excluded, "excluded")):
        for item in bucket:
            check_record_url(errors, item, name)
            if item.get("counts_as_video") is not False:
                fail(errors, f"{name} {item['id']} counts_as_video")

    readme = README.read_text(encoding="utf-8")
    if "skillry" in readme.lower():
        fail(errors, "README mentions the reference remake brand")
    sentinel = (
        f"seed={meta['seed_post_count']} gallery={meta['gallery_count']} "
        f"gallery_in_seed={meta['gallery_in_seed_count']} "
        f"gallery_resolved={meta['gallery_resolved_original_count']} "
        f"prompts={meta['prompt_file_count']} prompts_partial={meta['prompt_partial_count']} "
        f"context={meta['context_count']} excluded={meta['excluded_count']}"
    )
    if sentinel not in readme:
        fail(errors, "README count sentinel missing or stale")
    for phrase in (
        f"種子帖：{meta['seed_post_count']}",
        f"畫廊：{meta['gallery_count']}",
        f"種子內原帖：{meta['gallery_in_seed_count']}",
        f"轉載還原：{meta['gallery_resolved_original_count']}",
        f"公開提示詞：{meta['prompt_file_count']}",
        f"部分提示詞：{meta['prompt_partial_count']}",
        f"{meta['gallery_count']} gallery entries",
        f"{meta['seed_post_count']} seed posts",
        f"{meta['prompt_file_count']} public prompts",
    ):
        if phrase not in readme:
            fail(errors, f"README missing phrase: {phrase}")
    for key, label in CATEGORY_LABELS.items():
        heading = f"## {label}（{meta['category_counts'][key]}）"
        if heading not in readme:
            fail(errors, f"README missing heading {heading}")
    for item in gallery + context + excluded:
        if item["post_url"] not in readme:
            fail(errors, f"README missing {item['post_url']}")
    if "Asia/Shanghai" not in readme:
        fail(errors, "README has no Asia/Shanghai timestamp")
    if not LINKS.exists():
        fail(errors, "data/link-check.json missing; run python3 scripts/validate.py --links")
    else:
        link_data = json.loads(LINKS.read_text(encoding="utf-8"))
        by_url = {row["url"]: row for row in link_data["results"]}
        for item in gallery:
            for url in (item["post_url"], item["preview_url"]):
                row = by_url.get(url)
                if not row:
                    fail(errors, f"link check missing {url}")
                elif row["class"] == "dead":
                    fail(errors, f"gallery url dead: {url}")
                elif row["class"] not in {"ok", "blocked"}:
                    fail(errors, f"gallery url {row['class']}: {url}")
        summary = Counter(row["class"] for row in link_data["results"])
        if summary != Counter(link_data["summary"]):
            fail(errors, "link-check summary does not match rows")
    return errors


def classify_http(status: int, body: str, url: str) -> str:
    if status in {404, 410}:
        return "dead"
    if status in {401, 403, 429}:
        return "blocked"
    if status == 200:
        if "x.com/" in url or "twitter.com/" in url:
            status_id = url.rstrip("/").split("/")[-1]
            if status_id and status_id not in body and url not in body:
                return "blocked"
        return "ok"
    if status >= 500 or status == 0:
        return "error"
    return "blocked"


def fetch(url: str, method: str = "GET") -> tuple[int, str]:
    req = Request(url, method=method, headers={"User-Agent": "awesome-6.2-sol-videos-validator"})
    try:
        with urlopen(req, timeout=25) as response:
            raw = response.read(180_000)
            return response.status, raw.decode("utf-8", "replace")
    except HTTPError as exc:
        body = exc.read(80_000).decode("utf-8", "replace") if exc.fp else ""
        return exc.code, body
    except URLError as exc:
        return 0, str(exc)


def refresh_links(data: dict) -> None:
    urls: list[tuple[str, str]] = []
    seen: set[str] = set()

    def add(url: str, kind: str) -> None:
        if url and url not in seen:
            seen.add(url)
            urls.append((url, kind))

    for item in data["gallery"]:
        add(item["post_url"], "post")
        add(item["preview_url"], "preview")
    for item in data["context"] + data["excluded"]:
        add(item["post_url"], "post")
    for url in data["meta"].get("extra_checked_urls", []):
        add(url, "external")

    results = []
    for url, kind in urls:
        method = "HEAD" if kind == "preview" else "GET"
        status, body = fetch(url, method)
        if kind == "preview" and status in {405, 501}:
            status, body = fetch(url, "GET")
        results.append(
            {
                "url": url,
                "kind": kind,
                "http_status": status,
                "class": classify_http(status, body, url),
            }
        )
        print(f"{results[-1]['class']:7} {status:3} {kind:8} {url}", flush=True)
    summary = dict(Counter(row["class"] for row in results))
    for key in ("ok", "blocked", "dead", "error"):
        summary.setdefault(key, 0)
    payload = {
        "checked_at": datetime.now(SH).strftime("%Y-%m-%d %H:%M:%S Asia/Shanghai(UTC+8)"),
        "method": "GET post pages (x.com HTML must contain the status id); HEAD preview images on pbs.twimg.com",
        "summary": summary,
        "results": results,
    }
    LINKS.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wrote", LINKS, summary)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--links", action="store_true", help="recheck URLs and rewrite data/link-check.json")
    args = parser.parse_args()
    data = load()
    if args.links:
        refresh_links(data)
        data = load()
    errors = check(data)
    if errors:
        print(f"{len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    meta = data["meta"]
    print(
        f"ok gallery={meta['gallery_count']} prompts={meta['prompt_file_count']} "
        f"seed={meta['seed_post_count']} context={meta['context_count']} excluded={meta['excluded_count']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
