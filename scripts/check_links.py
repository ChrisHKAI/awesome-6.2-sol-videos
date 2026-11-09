#!/usr/bin/env python3
"""Record HTTP status for catalog post URLs. Response bodies are discarded."""

from __future__ import annotations

import json
import re
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from html import unescape
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data" / "videos.json"
OUTPUT = ROOT / "data" / "link-check.json"
USER_AGENT = "awesome-6.2-sol-videos-linkcheck/1.0"


def og_image(html: str) -> str | None:
    match = re.search(r'property="og:image" content="([^"]+)"', html)
    if not match:
        return None
    url = unescape(match.group(1)).strip()
    if url.startswith("https://pbs.twimg.com/"):
        return url
    return None


def check(url: str) -> dict:
    try:
        completed = subprocess.run(
            [
                "curl",
                "-sS",
                "-L",
                "--max-redirs",
                "5",
                "--max-time",
                "30",
                "-A",
                USER_AGENT,
                "-w",
                "\n%{http_code}",
                url,
            ],
            check=False,
            capture_output=True,
            text=True,
        )
    except OSError as exc:
        return {"url": url, "status": None, "error": str(exc), "og_image": None}
    if completed.returncode != 0:
        error = (completed.stderr or "").strip() or f"curl exit {completed.returncode}"
        return {"url": url, "status": None, "error": error, "og_image": None}
    body, _, code = completed.stdout.rpartition("\n")
    if not code.isdigit():
        return {"url": url, "status": None, "error": f"unexpected curl status {code!r}", "og_image": None}
    return {"url": url, "status": int(code), "error": None, "og_image": og_image(body)}


def main() -> None:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    urls = list(dict.fromkeys(entry["post_url"] for entry in catalog["entries"]))
    results = []
    with ThreadPoolExecutor(max_workers=6) as pool:
        futures = [pool.submit(check, url) for url in urls]
        for future in as_completed(futures):
            results.append(future.result())
    order = {url: index for index, url in enumerate(urls)}
    results.sort(key=lambda item: order[item["url"]])
    histogram: dict[str, int] = {}
    for item in results:
        key = "error" if item["status"] is None else str(item["status"])
        histogram[key] = histogram.get(key, 0) + 1
    checked_at = datetime.now(ZoneInfo("Asia/Shanghai")).strftime("%Y-%m-%d %H:%M:%S Asia/Shanghai (UTC+8)")
    payload = {
        "checked_at": checked_at,
        "timezone": "Asia/Shanghai UTC+8",
        "method": "HTTP GET via curl -L. Status code and og:image on pbs.twimg.com are kept; the page body is discarded.",
        "note_zh": "狀態碼只代表抓取當下的 HTTP 回應。og:image 是該帖公開頁自己的預覽，本庫沒有下載成檔。沒有 og:image 時不另找圖片。",
        "url_count": len(results),
        "status_histogram": histogram,
        "results": results,
    }
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"checked {len(results)} urls at {checked_at}: {histogram}")


if __name__ == "__main__":
    main()
