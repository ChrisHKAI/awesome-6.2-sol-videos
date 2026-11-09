#!/usr/bin/env python3
"""Merge the seed snapshot with editorial decisions and write the catalog."""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from editorial import ENTRIES  # noqa: E402

SEED_PATH = ROOT / "data" / "seed" / "posts.json"
OUT_PATH = ROOT / "data" / "videos.json"
README_PATH = ROOT / "README.md"

CAPTURED_AT = "2026-11-09 08:56:26 Asia/Shanghai(UTC+8)"
MEDIA_NOTE = "本庫未封存預覽或影片。抓取當下沒有核到該帖公開頁的 og:image，所以不嵌圖。請看原帖，不要用別處的圖片代替。"
PREVIEW_NOTE = "檔案沒有收進本庫。圖址是抓取當下該帖公開頁自己的 og:image，不是本庫做的畫面，日後也可能失效。"
SUPPRESSED_NOTE = "這則不嵌預覽，避免被看成模型畫面。圖檔沒有收進本庫。"
PREVIEW_ROLES = {"gallery", "counterexample_visual"}
ATTRIBUTION_COMMUNITY = (
    "社群所稱的 GPT-6.2 Sol。這個名稱和「已被路由」都未經 OpenAI 確認；"
    "本庫沒有重跑該次輸出，也沒有核對模型身分。"
)

CATEGORIES = [
    ("threejs", "Three.js", "種子文字或標籤寫到 Three.js 的畫面。雪原小屋的標籤是「Three.js／3D」，沒有拆開，技術欄只記 3d。"),
    ("3d-scene", "3D、場景與互動", "3D、場景，或種子寫明的互動畫面。技術欄空白表示種子沒寫渲染器。這裡面明確寫到互動場景的，是 Simpson 住宅那一條。"),
    ("animation", "動畫", "種子描述了動作、系列動畫或動態測試。沒寫技術棧的欄位留空。"),
    ("drawing-svg", "繪像與 SVG", "程式繪像、SVG，以及一支 computer-use 縮時。computer-use 放在這裡，是因為種子描述的成品是繪製過程。"),
    ("comparison", "對照", "這節的重點是對照。媒介各條不同。結論都是發帖者的說法，不是官方評測。孫悟空那一條比的是 qoder 與 workbuddy，不是 Opus 5.5。"),
]

CONTEXT = [
    ("counterexample_visual", "視覺反例", "counterexamples", "這些帖有畫面，但作者的結論是否定或偏好另一邊。不放進示範畫廊，避免被讀成推薦案例。"),
    ("uncertain", "歸屬或成品不明", "uncertain", "種子沒有足夠資訊把它當成一支 GPT-6.2 Sol 畫面。未知就保持不明，不補情節。"),
    ("retelling", "轉述", "retellings", "轉述別人的示範或對照。原始作者若沒有出現在種子裡，就保持空白，不猜帳號。"),
    ("detection", "路由與檢測", "detection", "檢測問句、用量頁說法、知識截止題。都不是畫面案例。Tony Awards 與 Fable 5 的答案不能用來鑑定模型。"),
    ("cost_quota", "成本、耗時與額度", "cost", "時間、帳單與額度是發帖當下的用戶說法。種子沒有把這些帖收成一支可命名的畫面。"),
    ("opinion", "觀點、質疑與沒有具體畫面的自報", "opinion", "主張、質疑、行為觀察、自報路由。沒有可入庫的具體畫面。"),
    ("rumor", "背景傳聞", "rumors", "發布日、價格、別家博客一類的傳聞。官方未確認。"),
    ("roundup", "綜述", "roundups", "整理別人的帖。容易把官方預告和模型路由寫在一起，所以單獨列出。"),
    ("official_non_model", "官方貼文，不是模型範例", "official", "官方帳號的帖留在這裡，避免被當成 GPT-6.2 Sol 的發布影片。"),
    ("irrelevant", "與這次無關", "irrelevant", "種子裡已標明不是 6.2 Sol 的舊模型對照。"),
]


def load_seed():
    data = json.loads(SEED_PATH.read_text(encoding="utf-8"))
    posts = data["posts"]
    if len(posts) != data["count"]:
        raise SystemExit("seed count field does not match posts")
    if set(ENTRIES) != {post["id"] for post in posts}:
        raise SystemExit("editorial ids do not match the seed")
    return data, posts


def fmt_time(value: str) -> str:
    return value.replace("Asia/Shanghai(UTC+8)", "Asia/Shanghai (UTC+8)")


def fmt_int(value):
    if value is None:
        return "無數據"
    return f"{value:,}"


def attribution_for(role: str) -> dict:
    if role == "official_non_model":
        return {
            "model_name_status": "official_post_not_a_model_announcement",
            "routing_claim": "not_applicable",
            "official_release": False,
            "note_zh": "這是官方開發者帳的貼文，不是 GPT-6.2 Sol 的發布說明。",
        }
    if role == "irrelevant":
        return {
            "model_name_status": "not_about_this_model",
            "routing_claim": "not_applicable",
            "official_release": False,
            "note_zh": "這則不討論 GPT-6.2 Sol 的視覺輸出。",
        }
    return {
        "model_name_status": "unconfirmed_community_name",
        "routing_claim": "user_reported_unverified",
        "official_release": False,
        "note_zh": ATTRIBUTION_COMMUNITY,
    }


def load_previews() -> dict[str, str | None]:
    path = ROOT / "data" / "link-check.json"
    if not path.exists():
        return {}
    payload = json.loads(path.read_text(encoding="utf-8"))
    return {item["url"]: item.get("og_image") for item in payload["results"]}


def build_entry(post: dict, previews: dict[str, str | None]) -> dict:
    meta = ENTRIES[post["id"]]
    role = meta["role"]
    unknowns = ["prompt.exact_public_text"]
    preview = previews.get(post["url"]) if role in PREVIEW_ROLES else None
    if preview and not str(preview).startswith("https://pbs.twimg.com/"):
        preview = None
    if not preview:
        unknowns.append("media.preview_url")
    quoted_author = None
    if post["type"] == "引用":
        unknowns.append("quoted_author_handle")
    if not meta["tech_tags"]:
        unknowns.append("tech_tags")
    return {
        "id": post["id"],
        "slug": meta["slug"],
        "role": role,
        "counts_as_gallery": role == "gallery",
        "title_zh": meta["title_zh"],
        "title_en": meta["title_en"],
        "author_handle": post["handle"],
        "author_url": f"https://x.com/{post['handle']}",
        "post_url": post["url"],
        "post_type": post["type"],
        "quoted_author_handle": quoted_author,
        "is_test_flag": post["is_test"],
        "is_official": post["is_official"],
        "created_at_utc": post["created_at"],
        "created_at_shanghai": post["created_at_shanghai"],
        "gallery_category": meta["gallery_category"],
        "tech_tags": list(meta["tech_tags"]),
        "tech_evidence": meta["tech_evidence"],
        "comparison": meta["comparison"],
        "prompt": {
            "status": meta["prompt_status"],
            "exact_public_text": None,
            "file": None,
            "title_mentioned": meta["prompt_title"],
            "note_zh": meta["prompt_note_zh"],
            "quoted_question": meta["quoted_question"],
            "quote_fidelity": meta["quote_fidelity"],
            "paraphrase_zh": meta["paraphrase_zh"],
        },
        "media": {
            "archived": False,
            "preview_url": preview,
            "note_zh": PREVIEW_NOTE if preview else (MEDIA_NOTE if role in PREVIEW_ROLES else SUPPRESSED_NOTE),
        },
        "metrics_snapshot": {
            "views": post["views"],
            "likes": post["likes"],
            "bookmarks": post["bookmarks"],
            "retweets": post["retweets"],
            "quotes": post["quotes"],
            "replies": post["replies"],
            "captured_at": CAPTURED_AT,
            "note_zh": "拉取當下的公開數字，不是歷史曲線。",
        },
        "attribution": attribution_for(role),
        "seed_summary": post["summary"],
        "seed_tags": post["tags"],
        "exclusion_reason_zh": meta["exclusion_reason_zh"],
        "extra_note_zh": meta["extra_note_zh"],
        "see_also": list(meta["see_also"]),
        "same_post_detection": meta["same_post_detection"],
        "subtype": meta["subtype"],
        "unknowns": unknowns,
    }


def opus_mentioned(entry: dict) -> bool:
    return entry["comparison"]["is_comparison"] and "Opus 5.5" in entry["comparison"]["against"]


def build_document(seed: dict, entries: list[dict]) -> dict:
    roles = Counter(entry["role"] for entry in entries)
    categories = Counter(entry["gallery_category"] for entry in entries if entry["counts_as_gallery"])
    gallery = [entry for entry in entries if entry["counts_as_gallery"]]
    prompt_files = [entry for entry in entries if entry["prompt"]["file"]]
    return {
        "schema_version": "1.0.0",
        "name": "Awesome 6.2 Sol Videos",
        "language": "zh-Hant",
        "model": {
            "community_name": "GPT-6.2 Sol",
            "also_seen_as": ["6.2 Sol", "gpt-6.2-sol"],
            "official_status": "unconfirmed",
            "statement_zh": (
                "GPT-6.2 Sol 是未經官方確認的社群名稱，也是用戶對路由結果的歸因。"
                "它不是本庫認定的正式發布。OpenAI 沒有在這批種子裡宣布這個模型。"
            ),
        },
        "provenance": {
            "seed_path": "data/seed/posts.json",
            "seed_summary_path": "data/seed/summary.md",
            "seed_csv_path": "data/seed/posts.csv",
            "seed_collected_at": seed["collected_at"],
            "seed_baseline_collected_at": seed["baseline_collected_at"],
            "seed_count": seed["count"],
            "seed_test_flag_count": seed["test_count"],
            "seed_official_flag_count": seed["official_count"],
            "seed_background_rumor_count": seed["background_rumor_count"],
            "seed_merge_stats": seed["merge_stats"],
            "completeness_zh": (
                "高訊號精選，不是全站完備。分頁沒有做到底。"
                "任務說明裡的 38 篇是 2026-11-09 08:40 的基線；隨附檔案的最新合併是 91 篇。"
                "本庫以隨附檔案為準。"
            ),
            "timezone": "Asia/Shanghai UTC+8",
            "metrics_are": "collection_time_snapshots",
            "additional_x_search": False,
            "reference_collection": {
                "url": "https://github.com/yihui-dev/awesome-opus5-5-videos",
                "license": "MIT",
                "copyright": "Copyright (c) 2026 yihui-dev",
                "reused": "sectioned list, original-post links, separate prompt files, structured JSON",
                "not_reused": [
                    "entries",
                    "prompts",
                    "media",
                    "preview hosting",
                    "hosted duplicate counts",
                    "branding",
                ],
            },
        },
        "counts": {
            "seed_posts": len(entries),
            "gallery": len(gallery),
            "prompt_files": len(prompt_files),
            "exact_public_generation_prompts": sum(
                1 for entry in entries if entry["prompt"]["status"] == "exact_public"
            ),
            "partial_public_prompts": sum(
                1 for entry in entries if entry["prompt"]["status"] == "partial_public"
            ),
            "gallery_with_comparison": sum(
                1 for entry in gallery if entry["comparison"]["is_comparison"]
            ),
            "gallery_mentioning_opus_5_5": sum(1 for entry in gallery if opus_mentioned(entry)),
            "by_role": dict(roles),
            "by_gallery_category": dict(categories),
        },
        "entries": entries,
    }


def metrics_line(entry: dict) -> str:
    metrics = entry["metrics_snapshot"]
    parts = [
        f"瀏覽 {fmt_int(metrics['views'])}",
        f"喜歡 {fmt_int(metrics['likes'])}",
        f"書籤 {fmt_int(metrics['bookmarks'])}",
        f"轉發 {fmt_int(metrics['retweets'])}",
        f"引用 {fmt_int(metrics['quotes'])}",
        f"回覆 {fmt_int(metrics['replies'])}",
    ]
    return "、".join(parts)


def comparison_line(entry: dict) -> str | None:
    comparison = entry["comparison"]
    if not comparison["is_comparison"]:
        return None
    names = "、".join(comparison["against"])
    return f"對照：相對 {names}。{comparison['verdict_zh']}這是用戶側說法，不是官方比較，本庫未獨立驗證。"


def render_gallery_entry(entry: dict) -> str:
    lines = [
        f"### {entry['title_zh']}",
        "",
        (
            f"[@{entry['author_handle']}]({entry['post_url']}) · {entry['post_type']} · "
            f"{fmt_time(entry['created_at_shanghai'])}"
        ),
        "",
    ]
    if entry["media"]["preview_url"]:
        lines.extend(
            [
                f"[![{entry['author_handle']} 原帖公開預覽，本庫未封存]({entry['media']['preview_url']})]({entry['post_url']})",
                "",
            ]
        )
    lines.append(f"- 歸因：{entry['attribution']['note_zh']}")
    if entry["post_type"] == "引用":
        lines.append("- 被引用帳號：種子沒有記下，保持未知。原作品作者可能不是這則帖的發文者。")
    tech = "、".join(entry["tech_tags"]) if entry["tech_tags"] else "種子沒寫"
    evidence = {
        "seed_summary": "寫在種子摘要",
        "seed_tag": "寫在種子標籤",
        "not_stated": "種子沒寫",
    }[entry["tech_evidence"]]
    lines.append(f"- 技術：{tech}（{evidence}；本庫沒有打開成品核對）")
    compared = comparison_line(entry)
    if compared:
        lines.append(f"- {compared}")
    lines.append(f"- 提示詞：{entry['prompt']['note_zh']}")
    if entry["prompt"]["title_mentioned"]:
        lines.append(f"- 提示詞名稱：{entry['prompt']['title_mentioned']}。全文仍然沒有。")
    if entry["same_post_detection"]:
        lines.append("- 同帖裡的檢測問句不拿來鑑定模型，也不當成這支畫面的提示詞。")
    if entry["extra_note_zh"]:
        lines.append(f"- 補充：{entry['extra_note_zh']}")
    lines.append(f"- 媒體：{entry['media']['note_zh']}")
    lines.append(
        f"- 互動快照（{fmt_time(entry['metrics_snapshot']['captured_at'])}）：{metrics_line(entry)}。"
    )
    lines.append("")
    return "\n".join(lines)


def render_context_entry(entry: dict) -> str:
    lines = [
        (
            f"- [@{entry['author_handle']}]({entry['post_url']}) · {entry['title_zh']} · "
            f"{entry['post_type']} · {fmt_time(entry['created_at_shanghai'])}"
        ),
        f"  - 為何不進畫廊：{entry['exclusion_reason_zh']}",
        f"  - 歸因：{entry['attribution']['note_zh']}",
    ]
    compared = comparison_line(entry)
    if compared:
        lines.append(f"  - {compared}")
    if entry["prompt"]["quoted_question"]:
        lines.append(
            "  - 種子摘句（不是生成提示詞，也不能鑑定模型）："
            f"`{entry['prompt']['quoted_question']}`"
        )
    if entry["prompt"]["paraphrase_zh"]:
        lines.append(f"  - 轉述：{entry['prompt']['paraphrase_zh']}")
    if entry["media"]["preview_url"]:
        lines.append(
            f"[![{entry['author_handle']} 原帖公開預覽，本庫未封存]({entry['media']['preview_url']})]({entry['post_url']})"
        )
    if entry["extra_note_zh"]:
        lines.append(f"  - 補充：{entry['extra_note_zh']}")
    if entry["see_also"]:
        links = ", ".join(f"`{item}`" for item in entry["see_also"])
        lines.append(f"  - 種子可對上的相關帖 id：{links}")
    lines.append(f"  - 媒體：{entry['media']['note_zh']}")
    return "\n".join(lines)


def render_readme(document: dict) -> str:
    counts = document["counts"]
    by_role = counts["by_role"]
    by_cat = counts["by_gallery_category"]
    entries = document["entries"]
    gallery = [entry for entry in entries if entry["counts_as_gallery"]]

    def cat_count(key: str) -> int:
        return by_cat[key]

    toc = "\n".join(
        [
            "- [怎麼讀這份清單](#how-to-read)",
            "- [統計](#stats)",
            "- [畫廊](#gallery)",
            *[f"  - [{title}（{cat_count(key)}）](#{key})" for key, title, _note in CATEGORIES],
            "- [研究與脈絡](#context)",
            *[f"  - [{title}（{by_role[key]}）](#{anchor})" for key, title, anchor, _note in CONTEXT],
            "- [提示詞](#prompts)",
            "- [媒體](#media)",
            "- [貢獻](#contributing)",
            "- [授權與參考清單](#license)",
            "- [English note](#english)",
        ]
    )

    gallery_blocks = ["<h2 id=\"gallery\">畫廊</h2>", ""]
    gallery_blocks.append(
        "畫廊只收種子裡有具體畫面、而且發帖者把它當成 GPT-6.2 Sol（或其所稱的路由結果）的帖。"
        f"共 {counts['gallery']} 條。其中 {counts['gallery_with_comparison']} 條帶有作者自己的對照說法，"
        f"{counts['gallery_mentioning_opus_5_5']} 條點名 Opus 5.5。"
        "點名 Opus 的句子都加了標籤。反方畫面、轉述、檢測、額度、觀點和傳聞不計入這 31 條。"
    )
    gallery_blocks.append("")
    for key, title, note in CATEGORIES:
        group = [entry for entry in gallery if entry["gallery_category"] == key]
        group.sort(key=lambda entry: (-(entry["metrics_snapshot"]["views"] or 0), entry["id"]))
        gallery_blocks.append(f"<h2 id=\"{key}\">{title}（{len(group)}）</h2>")
        gallery_blocks.append("")
        gallery_blocks.append(note)
        gallery_blocks.append("")
        for entry in group:
            gallery_blocks.append(render_gallery_entry(entry))

    context_blocks = [
        "<h2 id=\"context\">研究與脈絡</h2>",
        "",
        "下面這些帖留在庫裡，是為了看清這波討論裡什麼不是畫面案例。它們不計入畫廊。",
        "Tony Awards、Fable 5、Tibo、Karpathy 這類答案，都不能當成可靠的模型鑑定。",
        "",
    ]
    for key, title, anchor, note in CONTEXT:
        group = [entry for entry in entries if entry["role"] == key]
        group.sort(key=lambda entry: (-(entry["metrics_snapshot"]["views"] or 0), entry["id"]))
        context_blocks.append(f"<h2 id=\"{anchor}\">{title}（{len(group)}）</h2>")
        context_blocks.append("")
        context_blocks.append(note)
        context_blocks.append("")
        if key == "detection":
            context_blocks.append(
                "種子裡逐字出現過的檢測問句只有下面幾句。寫法依原摘要，不另編題幹。"
                "答對、答錯，或介面上看到某個型號字串，都不證明對方就是 GPT-6.2 Sol。"
            )
            context_blocks.append("")
        for entry in group:
            context_blocks.append(render_context_entry(entry))
            context_blocks.append("")

    english_rows = []
    for entry in sorted(gallery, key=lambda item: item["title_en"].lower()):
        category = dict((key, title) for key, title, _note in CATEGORIES)[entry["gallery_category"]]
        english_rows.append(
            f"| {entry['title_en']} | [@{entry['author_handle']}]({entry['post_url']}) | {category} | {entry['post_type']} |"
        )

    role_rows = "\n".join(
        f"| {title} | {by_role[key]} | 否 |" for key, title, _anchor, _note in CONTEXT
    )
    text = f"""# Awesome 6.2 Sol Videos

社群公開貼文裡，被稱為 **GPT-6.2 Sol**（也寫作 6.2 Sol、`gpt-6.2-sol`）的視覺示範。

**GPT-6.2 Sol 不是已確認的官方發布名稱。** 每一條都只是用戶側歸因。OpenAI 沒有在這批種子裡宣布這個模型，本庫也沒有重跑任何輸出。

這份清單不代表 OpenAI、Anthropic，或其他模型廠商。沒有重製版，也沒有把別的模型案例改名放進來。

- 畫廊：**{counts['gallery']}** 條有具體畫面的社群示範
- 逐字收錄的生成提示詞：**{counts['prompt_files']}**
- 種子帖：**{counts['seed_posts']}**（高訊號精選，分頁沒有做到底，不是全站完備）
- 種子時間：{fmt_time(document['provenance']['seed_collected_at'])}
- 互動數字是該時刻的公開快照

<!-- counts: seed={counts['seed_posts']} gallery={counts['gallery']} prompt_files={counts['prompt_files']} -->

## 目錄

{toc}

<h2 id="how-to-read">怎麼讀這份清單</h2>

一條畫廊記錄固定包含原帖、作者、上海時間、技術欄、提示詞狀態、媒體狀態，以及歸因。技術欄只寫種子裡看得到的詞。種子沒寫的，就寫「種子沒寫」，不補成 Three.js 或其他框架。

`is_test=true` 只表示種子把它標成測評或檢測相關，不等於它是一支影片。引用帖若沒有被引用帳號，被引用者保持未知。

時間全部是 Asia/Shanghai (UTC+8)。未知值保持空值，不估。

<h2 id="stats">統計</h2>

| 項目 | 數量 | 計入畫廊 |
| --- | ---: | --- |
| 種子帖 | {counts['seed_posts']} |  |
| 種子標記 `is_test=true` | {document['provenance']['seed_test_flag_count']} | 否，這不是影片數 |
| 畫廊 | {counts['gallery']} | 是 |
| 畫廊中帶對照說法 | {counts['gallery_with_comparison']} | 是，已標明對象 |
| 畫廊中點名 Opus 5.5 | {counts['gallery_mentioning_opus_5_5']} | 是，只代表作者說法 |
| 逐字生成提示詞檔 | {counts['prompt_files']} |  |
{role_rows}

基線 38 篇是 2026-11-09 08:40 Asia/Shanghai (UTC+8) 的歷史標記。隨附 `summary.md` 的最新合併是 91 篇：基線之後先補 20 篇，再補入 33 篇去重增量。種子自標的背景／傳聞約 {document['provenance']['seed_background_rumor_count']} 篇；本庫改依「是不是視覺案例」分組，所以各節人數不會等於 14。

官方相關標記 {document['provenance']['seed_official_flag_count']} 篇，是 @OpenAIDevs 的「Tomorrow.」。它不是模型官宣。

{chr(10).join(gallery_blocks)}
{chr(10).join(context_blocks)}
<h2 id="prompts">提示詞（{counts['prompt_files']}）</h2>

`prompts/` 目前沒有提示詞正文。種子沒有一支畫面案例留下可逐字核對的公開生成提示詞，所以不建檔、不改寫、不把策展摘要假裝成作者原文。

《時間的盡頭》只是名稱。有的帖寫「同 prompt」或「詳細 prompt」，正文不在種子裡。檢測問句即使被摘要逐字記下，也不是生成提示詞，不放進 `prompts/`。

<h2 id="media">媒體</h2>

畫廊和視覺反例如果在抓取當下看得到該帖公開頁自己的預覽圖，頁面上會連過去。圖檔沒有下載進本庫，也沒有改畫。其他帖即使有預覽也不嵌，避免檢測截圖或官方預告被看成模型示範。沒有核到預覽的條目只留原帖連結。

連結檢查在 [`data/link-check.json`](data/link-check.json)。HTTP 狀態只說明抓取當下伺服器有回應，不證明帖文內容。

<h2 id="contributing">貢獻</h2>

補登方式見 [CONTRIBUTING.md](CONTRIBUTING.md)。不要為了這份清單去私訊作者。新的 X 檢索不在這次範圍裡。

<h2 id="license">授權與參考清單</h2>

本庫自己寫的說明、分類、結構描述與檢查程式，以 [MIT License](LICENSE) 釋出。著作權行使用倉庫所有者帳號 ChrisHKAI。

帖文、影片、圖片與提示詞仍屬原作者。本庫不替他們轉授權，也不把這些作品收進 MIT。

分區清單、原帖連結、提示詞分開存放、以及 `data/videos.json` 這種組織，參考 [yihui-dev/awesome-opus5-5-videos](https://github.com/yihui-dev/awesome-opus5-5-videos)（MIT License，Copyright (c) 2026 yihui-dev）。沒有複製該庫的條目、提示詞、預覽或重製數量，也沒有沿用它的預覽站品牌。

<h2 id="english">English note</h2>

GPT-6.2 Sol is an unconfirmed community name and routing attribution, not an official release. This repository does not speak for OpenAI. The gallery has {counts['gallery']} community-reported visual posts from a non-exhaustive snapshot of {counts['seed_posts']} posts, collected at {fmt_time(document['provenance']['seed_collected_at'])}. Metrics are snapshots from that collection. No exact public generation prompt was in the seed, so there are {counts['prompt_files']} prompt files. Gallery previews are the posts' own public image links and are not stored here. Other posts are not embedded. Tony Awards and Fable answers are not used as model identification. Comparisons, including those with Opus 5.5, are labeled author claims. The sectioned layout follows yihui-dev/awesome-opus5-5-videos (MIT); its entries, prompts, previews, hosted-count claims, and branding were not copied.

| Title | Author | Section | Post type |
| --- | --- | --- | --- |
{chr(10).join(english_rows)}
"""
    return text


def main() -> None:
    seed, posts = load_seed()
    entries = [build_entry(post, load_previews()) for post in posts]
    document = build_document(seed, entries)
    OUT_PATH.write_text(json.dumps(document, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    README_PATH.write_text(render_readme(document), encoding="utf-8")
    print(
        f"wrote {OUT_PATH.relative_to(ROOT)} and README.md "
        f"gallery={document['counts']['gallery']} prompts={document['counts']['prompt_files']}"
    )


if __name__ == "__main__":
    main()
