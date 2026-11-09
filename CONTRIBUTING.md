# 如何補充

這份清單收的是公開帖裡、作者歸因到「GPT-6.2 Sol」的**視覺演示**。名稱仍是未確認的社群叫法，不是已宣布的模型。

## 可以加進來的

- 原帖看得到畫面：影片、動圖，或作品本身的圖片。
- 作者自己的作品。轉貼別人的影片時，請改記原作者，不要把它算成新的一條。
- 提示詞必須是帖文裡能逐字核對的公開文字。只寫了「用了同一個 prompt」而沒貼出來，`prompt` 維持 `null`，不要補寫。
- 只看到一半、或還要靠沒附上的參考圖，`prompt_partial` 設為 `true`，並在註記寫明缺了什麼。

## 不要加進畫廊數字的

- 路由檢測、知識截止題（Tony Awards、Fable、Karpathy 這類）。這些題有反證，不能用來確認模型。
- 純意見、發布日傳聞、額度截圖。
- 官方帳號與模型無關的預告。
- 舊模型對照，例如 GPT-5.2。若有資料價值，放到 `context` 或 `excluded`，不要算進畫廊。
- 把 Opus 或其他模型的舊作品改名成 Sol。

和 Opus 或其他模型的對照可以收，但 `comparison_with` 要寫明對照對象，並且註明標籤來自作者，不是本庫復現。

## 送出前

1. 在 `data/videos.json` 加上條目。`attribution` 用 `creator_reported`，`independently_reproduced` 維持 `false`。
2. 時間寫 Asia/Shanghai（UTC+8）。互動數字註明是哪一次快照。
3. 有提示詞才新增 `prompts/<slug>.md`，Prompt 區塊與 JSON 逐字相同。
4. 預覽只用可追溯的公開縮圖。不要把完整影片檔放進倉庫。
5. 跑 `python3 scripts/validate.py`。它會核對 id、網址、去重、提示詞檔，以及 README 上的數字。

創作者要求修改或撤下自己的作品時，請開 issue。本庫會改連結或移除條目，不會主張那些作品的著作權。
