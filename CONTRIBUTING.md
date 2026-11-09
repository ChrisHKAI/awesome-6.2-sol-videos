# 貢獻

這份清單收的是社群公開帖裡、被稱為 GPT-6.2 Sol 的視覺示範。名稱尚未經官方確認。補資料時維持這個口徑。

## 可以補什麼

- 一則公開帖，而且帖裡看得到具體畫面
- 原帖連結、作者帳號、發文時間（Asia/Shanghai，UTC+8）
- 種子或你親眼看到的技術名稱。沒看到就留空，不要補成 Three.js
- 逐字出現在公開帖裡的生成提示詞

## 不要放進畫廊

- 只有路由檢測、Tony Awards、Fable 5、Tibo、Karpathy 或其他知識題。這些答案不能鑑定模型
- 純觀點、發布日傳聞、額度或帳單故事，而且沒有可命名的畫面
- 官方預告，除非該帖本身就是在發布這個模型。目前的「Tomorrow.」不是
- GPT-5.2 或其他舊模型的對照
- 轉述。轉述放在研究區，並盡量指向原始帖；不知道原作者就留空

對照可以收，但必須寫明比較對象，以及那是作者說法。反方畫面放在視覺反例，不放進畫廊。

## 提示詞檔

只有公開帖裡的逐字文本才能放進 `prompts/`。檔名用條目的 `slug`。檔案開頭標明狀態：

- `exact_public`：公開全文
- `partial_public`：只公開了片段，檔內不得把缺的部分補完

策展摘要、標題和「作者說有很長的 prompt」都不是提示詞檔。沒有逐字文本時，`prompt.file` 保持 `null`，`exact_public_text` 保持 `null`。

## 媒體

不要嵌未核對的預覽，不要用圖庫素材，不要把別的模型影片改名。沒有可核對的公開預覽時，保持 `media.archived=false` 與 `preview_url=null`，並在說明裡寫媒體未封存。

## 不要做的事

- 不要為了補這份清單私訊作者，或替作者發文
- 不要把互動數字改成後來看到的新數字，除非連同抓取時間一起更新
- 不要把 91 或以後的總數寫成全站完備

## 改完後

從倉庫根目錄執行：

```bash
python3 scripts/build_catalog.py
python3 scripts/check_links.py
python3 scripts/build_catalog.py
python3 scripts/validate.py
```

`build_catalog.py` 會依 `data/seed/posts.json`、`scripts/editorial.py` 與已有的 `data/link-check.json` 重寫 `data/videos.json` 和 `README.md`。手改這兩個產出檔會在下次建置時被蓋掉。連結檢查只留下 HTTP 狀態和公開頁的預覽圖址，不保存頁面正文。第二次建置才會把畫廊預覽寫進清單。
