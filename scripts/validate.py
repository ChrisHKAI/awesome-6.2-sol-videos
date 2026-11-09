#!/usr/bin/env python3
"""Check ids, URLs, prompt files, and README counts against the catalog."""

from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from editorial import ENTRIES  # noqa: E402

DENY = set("这为对与后发录国经视预确从还让给门问库数实测样并应进将个时东车长云网页动类当没现开关于仅过经条验频览认题据试说边该画场别")
PROMPT_FILE_STATUSES = {"exact_public", "partial_public"}
CATEGORY_IDS = {
    "threejs": "Three.js",
    "3d-scene": "3D、場景與互動",
    "animation": "動畫",
    "drawing-svg": "繪像與 SVG",
    "comparison": "對照",
}
ROLE_HEADINGS = {
    "counterexample_visual": ("counterexamples", "視覺反例"),
    "uncertain": ("uncertain", "歸屬或成品不明"),
    "retelling": ("retellings", "轉述"),
    "detection": ("detection", "路由與檢測"),
    "cost_quota": ("cost", "成本、耗時與額度"),
    "opinion": ("opinion", "觀點、質疑與沒有具體畫面的自報"),
    "rumor": ("rumors", "背景傳聞"),
    "roundup": ("roundups", "綜述"),
    "official_non_model": ("official", "官方貼文，不是模型範例"),
    "irrelevant": ("irrelevant", "與這次無關"),
}


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []

    def check(self, condition: bool, message: str) -> None:
        if not condition:
            self.errors.append(message)


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    report = Report()
    seed = load_json(ROOT / "data" / "seed" / "posts.json")
    posts = seed["posts"]
    catalog = load_json(ROOT / "data" / "videos.json")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    entries = catalog["entries"]

    report.check(seed["count"] == len(posts) == 91, "seed count is not 91")
    report.check(len({post["id"] for post in posts}) == len(posts), "seed ids are not unique")
    with (ROOT / "data" / "seed" / "posts.csv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    report.check({row["id"] for row in rows} == {post["id"] for post in posts}, "csv ids differ from json")
    report.check(len(rows) == len(posts), "csv row count differs from json")

    report.check(set(ENTRIES) == {post["id"] for post in posts}, "editorial coverage drifted")
    report.check(len(entries) == len(posts), "catalog size differs from the seed")
    report.check(len({entry["id"] for entry in entries}) == len(entries), "catalog ids are not unique")
    report.check({entry["id"] for entry in entries} == {post["id"] for post in posts}, "catalog ids differ from the seed")
    report.check(len({entry["slug"] for entry in entries}) == len(entries), "slugs are not unique")
    report.check(len({entry["post_url"] for entry in entries}) == len(entries), "post URLs are not unique")

    posts_by_id = {post["id"]: post for post in posts}
    roles = Counter()
    categories = Counter()
    prompt_files = []
    for entry in entries:
        post = posts_by_id[entry["id"]]
        meta = ENTRIES[entry["id"]]
        roles[entry["role"]] += 1
        report.check(entry["role"] == meta["role"], f"{entry['id']} role drifted")
        report.check(entry["slug"] == meta["slug"], f"{entry['id']} slug drifted")
        report.check(entry["post_url"] == post["url"], f"{entry['id']} url drifted")
        report.check(entry["author_handle"] == post["handle"], f"{entry['id']} handle drifted")
        report.check(entry["author_url"] == f"https://x.com/{post['handle']}", f"{entry['id']} author url")
        report.check(entry["post_url"].startswith("https://x.com/"), f"{entry['id']} url scheme")
        report.check(entry["created_at_shanghai"] == post["created_at_shanghai"], f"{entry['id']} time drifted")
        report.check(entry["created_at_shanghai"].endswith("Asia/Shanghai(UTC+8)"), f"{entry['id']} timezone")
        report.check(entry["is_test_flag"] is post["is_test"], f"{entry['id']} test flag")
        report.check(entry["is_official"] is post["is_official"], f"{entry['id']} official flag")
        report.check(entry["seed_summary"] == post["summary"], f"{entry['id']} summary drifted")
        report.check(entry["attribution"]["official_release"] is False, f"{entry['id']} official release flag")
        report.check(entry["media"]["archived"] is False, f"{entry['id']} media archived")
        preview = entry["media"]["preview_url"]
        if preview is not None:
            report.check(preview.startswith("https://pbs.twimg.com/"), f"{entry['id']} preview host")
            report.check(entry["role"] in {"gallery", "counterexample_visual"}, f"{entry['id']} preview on a non-visual role")
        else:
            report.check("media.preview_url" in entry["unknowns"], f"{entry['id']} missing preview unknown")
        report.check(entry["prompt"]["exact_public_text"] is None, f"{entry['id']} prompt text was invented")
        report.check(entry["prompt"]["file"] is None, f"{entry['id']} prompt file was set")
        status = entry["prompt"]["status"]
        if status == "named_only":
            report.check(bool(entry["prompt"]["title_mentioned"]), f"{entry['id']} named prompt lacks a title")
        else:
            report.check(entry["prompt"]["title_mentioned"] is None, f"{entry['id']} unexpected prompt title")
        report.check(status not in PROMPT_FILE_STATUSES, f"{entry['id']} claims a prompt file status")
        if entry["prompt"]["quoted_question"] is not None:
            report.check(status == "not_a_generation_prompt", f"{entry['id']} quoted question stored as a generation prompt")
            report.check(entry["prompt"]["quote_fidelity"] == "seed_summary_quotation", f"{entry['id']} quote fidelity")
        comparison = entry["comparison"]
        if comparison["is_comparison"]:
            report.check(bool(comparison["against"]) and bool(comparison["verdict_zh"]), f"{entry['id']} comparison fields")
        else:
            report.check(comparison["against"] == [] and comparison["verdict_zh"] is None, f"{entry['id']} empty comparison")
        for key in ("views", "likes", "bookmarks", "retweets", "quotes", "replies"):
            value = entry["metrics_snapshot"][key]
            report.check(value is None or isinstance(value, int), f"{entry['id']} metric {key}")
            report.check(entry["metrics_snapshot"][key] == post[key], f"{entry['id']} metric {key} drifted")
        report.check(entry["metrics_snapshot"]["captured_at"] == seed["collected_at"], f"{entry['id']} metric time")
        if entry["tech_tags"]:
            report.check(entry["tech_evidence"] in {"seed_summary", "seed_tag"}, f"{entry['id']} tech evidence")
        else:
            report.check(entry["tech_evidence"] == "not_stated", f"{entry['id']} tech evidence")
        if entry["post_type"] == "引用":
            report.check(entry["quoted_author_handle"] is None, f"{entry['id']} quoted author filled")
            report.check("quoted_author_handle" in entry["unknowns"], f"{entry['id']} quote unknown")
        else:
            report.check("quoted_author_handle" not in entry["unknowns"], f"{entry['id']} quote unknown on original")
        if entry["counts_as_gallery"]:
            report.check(entry["role"] == "gallery", f"{entry['id']} gallery role")
            report.check(entry["exclusion_reason_zh"] is None, f"{entry['id']} gallery has an exclusion")
            report.check(entry["gallery_category"] in CATEGORY_IDS, f"{entry['id']} category")
            categories[entry["gallery_category"]] += 1
        else:
            report.check(entry["gallery_category"] is None, f"{entry['id']} non-gallery category")
            report.check(bool(entry["exclusion_reason_zh"]), f"{entry['id']} missing exclusion reason")
        if entry["role"] == "opinion":
            report.check(bool(entry["subtype"]), f"{entry['id']} opinion subtype")
        else:
            report.check(entry["subtype"] is None, f"{entry['id']} unexpected subtype")
        for related in entry["see_also"]:
            report.check(related in posts_by_id and related != entry["id"], f"{entry['id']} see_also {related}")
        if entry["prompt"]["file"]:
            prompt_files.append(entry["prompt"]["file"])

    report.check(roles["gallery"] == 31, f"gallery count is {roles['gallery']}")
    report.check(sum(roles.values()) == 91, "role counts do not add up to 91")
    report.check(catalog["counts"]["seed_posts"] == 91, "count block seed")
    report.check(catalog["counts"]["gallery"] == roles["gallery"], "count block gallery")
    report.check(catalog["counts"]["prompt_files"] == 0, "count block prompts")
    report.check(catalog["counts"]["exact_public_generation_prompts"] == 0, "exact prompts")
    report.check(catalog["counts"]["partial_public_prompts"] == 0, "partial prompts")
    report.check(catalog["counts"]["by_role"] == dict(roles), "by_role drifted")
    report.check(catalog["counts"]["by_gallery_category"] == dict(categories), "by category drifted")
    gallery_entries = [entry for entry in entries if entry["counts_as_gallery"]]
    report.check(
        catalog["counts"]["gallery_with_comparison"]
        == sum(1 for entry in gallery_entries if entry["comparison"]["is_comparison"]),
        "comparison count",
    )
    report.check(
        catalog["counts"]["gallery_mentioning_opus_5_5"]
        == sum(
            1
            for entry in gallery_entries
            if entry["comparison"]["is_comparison"] and "Opus 5.5" in entry["comparison"]["against"]
        ),
        "opus count",
    )

    on_disk = sorted(path.name for path in (ROOT / "prompts").glob("*") if path.name != "README.md")
    report.check(on_disk == [], f"unexpected prompt files: {on_disk}")
    report.check(prompt_files == [], "catalog points at prompt files")
    report.check((ROOT / "prompts" / "README.md").is_file(), "prompts/README.md missing")

    count_comment = re.search(r"<!-- counts: seed=(\d+) gallery=(\d+) prompt_files=(\d+) -->", readme)
    report.check(count_comment is not None, "README count comment missing")
    if count_comment:
        report.check(tuple(int(part) for part in count_comment.groups()) == (91, roles["gallery"], 0), "README count comment")

    for key, title in CATEGORY_IDS.items():
        report.check(f'<h2 id="{key}">{title}（{categories[key]}）</h2>' in readme, f"heading {title}")
    for role, (anchor, title) in ROLE_HEADINGS.items():
        report.check(f'<h2 id="{anchor}">{title}（{roles[role]}）</h2>' in readme, f"heading {title}")
    report.check(f"<h2 id=\"prompts\">提示詞（0）</h2>" in readme, "prompt heading")
    report.check(len(re.findall(r"^### ", readme, flags=re.M)) == roles["gallery"], "gallery entry headings")
    report.check("Skillry" not in readme, "preview-site brand leaked into README")
    report.check("remake" not in readme.lower(), "remake wording leaked into README")
    leaked = sorted({char for char in readme if char in DENY})
    report.check(not leaked, f"simplified characters in README: {''.join(leaked)}")
    for relative in ("CONTRIBUTING.md", "prompts/README.md", "NOTICE.md"):
        text = (ROOT / relative).read_text(encoding="utf-8")
        leaked = sorted({char for char in text if char in DENY})
        report.check(not leaked, f"simplified characters in {relative}: {''.join(leaked)}")

    link_check = load_json(ROOT / "data" / "link-check.json")
    results = link_check["results"]
    result_urls = [item["url"] for item in results]
    report.check(len(result_urls) == len(set(result_urls)), "duplicate link-check urls")
    report.check(set(result_urls) == {entry["post_url"] for entry in entries}, "link-check coverage")
    by_url = {item["url"]: item for item in results}
    for entry in entries:
        item = by_url[entry["post_url"]]
        report.check("og_image" in item, f"og_image missing for {entry['id']}")
        og_image = item.get("og_image")
        if og_image is not None:
            report.check(og_image.startswith("https://pbs.twimg.com/"), f"og host {entry['id']}")
        if entry["role"] in {"gallery", "counterexample_visual"}:
            report.check(entry["media"]["preview_url"] == og_image, f"preview mismatch {entry['id']}")
            if og_image:
                report.check(og_image in readme, f"README missing preview {entry['id']}")
        else:
            report.check(entry["media"]["preview_url"] is None, f"non-visual preview {entry['id']}")
    shown = {entry["media"]["preview_url"] for entry in entries if entry["media"]["preview_url"]}
    for entry in entries:
        if entry["role"] in {"gallery", "counterexample_visual"}:
            continue
        og_image = by_url[entry["post_url"]].get("og_image")
        if og_image and og_image not in shown:
            report.check(og_image not in readme, f"README shows a non-gallery preview {entry['id']}")
    for item in results:
        status = item["status"]
        error = item["error"]
        report.check(isinstance(status, int) or (status is None and error), f"unchecked url {item['url']}")
        report.check("body" not in item, "link-check stored a body")
    report.check(bool(link_check.get("checked_at")), "link-check time missing")
    report.check("Asia/Shanghai" in link_check["checked_at"], "link-check timezone")

    if report.errors:
        print(f"{len(report.errors)} validation error(s):")
        for error in report.errors:
            print(f"- {error}")
        return 1
    print(
        "validation passed: "
        f"seed=91 gallery={roles['gallery']} prompt_files=0 "
        f"roles={dict(roles)} categories={dict(categories)} "
        f"links={len(results)}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
