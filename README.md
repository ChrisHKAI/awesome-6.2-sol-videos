# Awesome 6.2 Sol Videos

**English.** 34 gallery entries, 5 public prompts, 91 seed posts. This is a list of public visual demos whose authors attributed them to “GPT-6.2 Sol” in a snapshot taken 2026-11-09 (Asia/Shanghai, UTC+8). That name is a community label. OpenAI had not announced it as a model in this collection, and nothing here was independently reproduced. Each entry links to the original post. A prompt file exists only when the author published the exact wording; otherwise the prompt is null. Knowledge-cutoff quizzes are not a reliable way to tell which model answered.

<!-- seed=91 gallery=34 gallery_in_seed=33 gallery_resolved=1 prompts=5 prompts_partial=3 context=57 excluded=1 -->

社群把一批畫面稱作 **GPT-6.2 Sol**。這份清單收集那些**看得到畫面**的公開演示；作者若把提示詞原文貼了出來，就按字收進 [`prompts/`](prompts/)。

這些帖是作者自己說被路由到這個名稱之後發出的。**OpenAI 沒有在這批材料裡宣布這個模型。** 本庫沒有重跑任何一條，也沒有把別的模型的舊作品改名放進來。預覽圖是原帖的公開縮圖，完整影片不下載、不轉存。縮圖失效時，以原帖為準。

挑選一條，打開原帖。有提示詞檔就複製 Prompt 區塊，拿到你自己的程式代理裡試；原作若是 Three.js 或 SVG，請它交一個 HTML。做出類似的畫面，**不能**證明你用到的是同一個模型。

- 種子帖：91（蒐集於 2026-11-09 08:56:26 Asia/Shanghai(UTC+8)；其中 2026-11-09 08:40:28 Asia/Shanghai(UTC+8) 的基線是 38 篇，本庫以合併後的 91 篇為範圍）
- 畫廊：34（種子內原帖：33；轉載還原：1）
- 公開提示詞：5（部分提示詞：3；其餘畫廊條目的 prompt 為 null）
- 種子裡 `is_test=true` 有 71 篇。那個旗標只表示測評或檢測相關，不是 71 支影片
- 畫面與帖文核對於 2026-11-09 09:15:08 Asia/Shanghai(UTC+8)。互動數字是種子蒐集當下，不是即時

同一支媒體的轉貼、純意見、路由檢測、官方「Tomorrow.」預告，以及一則 GPT-5.2 舊基準，都不在這 34 條裡面。

## 目錄

- [Three.js 與 3D 場景](#cat-3d)（15）
- [角色、動態與繪像](#cat-character)（9）
- [對照](#cat-comparison)（10）
- [提示詞怎麼用](#how-to-use)
- [脈絡，不計入畫廊](#context)
- [已排除](#excluded)
- [授權與出處](#credits)

<a id="cat-3d"></a>
## Three.js 與 3D 場景（15）

<table>
<tr><td width="33%" valign="top"><a href="https://x.com/TokenGremlin/status/2119371334878744648"><img src="https://pbs.twimg.com/amplify_video_thumb/2119371292654653440/img/dmoCx4RO8lnEQtbn.jpg" alt="雲上宮殿" width="100%"></a><br><a href="https://x.com/TokenGremlin/status/2119371334878744648"><b>雲上宮殿</b></a><br><a href="https://x.com/TokenGremlin">@TokenGremlin</a> · 提示詞未公開<br><sub>Three.js · 單檔 HTML · 作者自述</sub><br><sub>作者把畫面歸到尚未被官方確認的 GPT-6.2 Sol。</sub></td><td width="33%" valign="top"><a href="https://x.com/TokenGremlin/status/2119395930805879165"><img src="https://pbs.twimg.com/amplify_video_thumb/2119394874591944704/img/F0D_beICGEBB-esh.jpg" alt="單次生成的黑洞" width="100%"></a><br><a href="https://x.com/TokenGremlin/status/2119395930805879165"><b>單次生成的黑洞</b></a><br><a href="https://x.com/TokenGremlin">@TokenGremlin</a> · 提示詞未公開<br><sub>Three.js · 單檔 HTML · 作者自述 · 對照 Opus 5.5</sub><br><sub>「勝過 Opus 5.5」是作者自述，不是並排對照片。</sub></td><td width="33%" valign="top"><a href="https://x.com/TokenGremlin/status/2119409785900552548"><img src="https://pbs.twimg.com/amplify_video_thumb/2119409755286384640/img/FUyYzAl2XbSN0HDB.jpg" alt="櫻花村莊" width="100%"></a><br><a href="https://x.com/TokenGremlin/status/2119409785900552548"><b>櫻花村莊</b></a><br><a href="https://x.com/TokenGremlin">@TokenGremlin</a> · 提示詞未公開<br><sub>Three.js · 單檔 HTML · 作者自述 · 對照 GPT-6 Astra</sub><br><sub>和 Astra 的高下是作者自述。</sub></td></tr>
<tr><td width="33%" valign="top"><a href="https://x.com/kimmonismus/status/2119543483048268179"><img src="https://pbs.twimg.com/media/HWoXoNBWAAAOdSM.jpg?name=large" alt="鵜鶘，以及辛普森街景" width="100%"></a><br><a href="https://x.com/kimmonismus/status/2119543483048268179"><b>鵜鶘，以及辛普森街景</b></a><br><a href="https://x.com/kimmonismus">@kimmonismus</a> · 提示詞未公開<br><sub>Three.js · 作者自述</sub><br><sub>作者自己在模型名稱後面加了問號。</sub></td><td width="33%" valign="top"><a href="https://x.com/Khazix0918/status/2119507514459144677"><img src="https://pbs.twimg.com/amplify_video_thumb/2119507467990413312/img/dCMmCV5ohy_PaqTY.jpg" alt="時間的盡頭" width="100%"></a><br><a href="https://x.com/Khazix0918/status/2119507514459144677"><b>時間的盡頭</b></a><br><a href="https://x.com/Khazix0918">@Khazix0918</a> · <a href="prompts/khazix0918-144677.md">提示詞</a><br><sub>Three.js · 作者自述</sub></td><td width="33%" valign="top"><a href="https://x.com/Mr_Salio/status/2119437812604838342"><img src="https://pbs.twimg.com/amplify_video_thumb/2119437684120707072/img/hWdo-zoXb1i1TRWG.jpg" alt="浮島與高塔" width="100%"></a><br><a href="https://x.com/Mr_Salio/status/2119437812604838342"><b>浮島與高塔</b></a><br><a href="https://x.com/Mr_Salio">@Mr_Salio</a> · 提示詞未公開<br><sub>純代碼 · 作者自述 · 對照 GPT-6.1 Sol</sub><br><sub>和 6.1 的比較是作者自述，畫面裡沒有並排。</sub></td></tr>
<tr><td width="33%" valign="top"><a href="https://x.com/Mr_Salio/status/2119464940964593751"><img src="https://pbs.twimg.com/amplify_video_thumb/2119464564764913664/img/_LzQaPJ_Lq4zHDW3.jpg" alt="月下燈塔與海面" width="100%"></a><br><a href="https://x.com/Mr_Salio/status/2119464940964593751"><b>月下燈塔與海面</b></a><br><a href="https://x.com/Mr_Salio">@Mr_Salio</a> · 提示詞未公開<br><sub>純代碼 · 作者自述</sub></td><td width="33%" valign="top"><a href="https://x.com/JustinGorya/status/2119421717290381531"><img src="https://pbs.twimg.com/media/HWmypG6WoAApirI.jpg?name=large" alt="AK-47 渲染" width="100%"></a><br><a href="https://x.com/JustinGorya/status/2119421717290381531"><b>AK-47 渲染</b></a><br><a href="https://x.com/JustinGorya">@JustinGorya</a> · 提示詞未公開<br><sub>3D · 作者自述</sub><br><sub>路由仍是作者懷疑。</sub></td><td width="33%" valign="top"><a href="https://x.com/ai_funss/status/2119445773909926181"><img src="https://pbs.twimg.com/amplify_video_thumb/2119443779702628352/img/3Whi9cqn7B9dbRzm.jpg" alt="浮世繪巨浪" width="100%"></a><br><a href="https://x.com/ai_funss/status/2119445773909926181"><b>浮世繪巨浪</b></a><br><a href="https://x.com/ai_funss">@ai_funss</a> · 提示詞未公開<br><sub>Three.js · 單檔 HTML · 作者自述 · 對照 Opus 5.5</sub><br><sub>「不弱於 Opus 5.5」是作者判斷，預覽不是並排對照。</sub></td></tr>
<tr><td width="33%" valign="top"><a href="https://x.com/FiniYang/status/2119481246627799067"><img src="https://pbs.twimg.com/amplify_video_thumb/2119481119888584704/img/TeHdzS_9vnPBMR8v.jpg" alt="黑洞，第二彈" width="100%"></a><br><a href="https://x.com/FiniYang/status/2119481246627799067"><b>黑洞，第二彈</b></a><br><a href="https://x.com/FiniYang">@FiniYang</a> · 提示詞未公開<br><sub>作者自述</sub><br><sub>技術棧作者沒有寫明。</sub></td><td width="33%" valign="top"><a href="https://x.com/bei351009016/status/2119459756435710212"><img src="https://pbs.twimg.com/amplify_video_thumb/2119444741733699584/img/zoH4BoAdRjr9l-e4.jpg" alt="雪原小屋" width="100%"></a><br><a href="https://x.com/bei351009016/status/2119459756435710212"><b>雪原小屋</b></a><br><a href="https://x.com/bei351009016">@bei351009016</a> · 提示詞未公開<br><sub>Three.js · HTML · 作者自述</sub><br><sub>正文寫 GPT6.2，介面標 GPT-6.1 Sol Max。</sub></td><td width="33%" valign="top"><a href="https://x.com/FiniYang/status/2119495861852160420"><img src="https://pbs.twimg.com/amplify_video_thumb/2119495532892880897/img/4g6dCSMgvb_YD9H0.jpg" alt="雨夜巷子" width="100%"></a><br><a href="https://x.com/FiniYang/status/2119495861852160420"><b>雨夜巷子</b></a><br><a href="https://x.com/FiniYang">@FiniYang</a> · 提示詞未公開<br><sub>作者自述</sub></td></tr>
<tr><td width="33%" valign="top"><a href="https://x.com/LJL06019/status/2119479647192920395"><img src="https://pbs.twimg.com/amplify_video_thumb/2119479507346423808/img/1AxAjTRHzpuHNbR9.jpg" alt="手機裡的黑洞觀測台" width="100%"></a><br><a href="https://x.com/LJL06019/status/2119479647192920395"><b>手機裡的黑洞觀測台</b></a><br><a href="https://x.com/LJL06019">@LJL06019</a> · 提示詞未公開<br><sub>作者自述 · 對照 Opus 5.5</sub><br><sub>「爆打 Opus 5.5」只有作者結論，沒有並排畫面。</sub></td><td width="33%" valign="top"><a href="https://x.com/FiniYang/status/2119583244937314674"><img src="https://pbs.twimg.com/amplify_video_thumb/2119515616092782592/img/2LCumaDxYvr7RY4b.jpg" alt="懸霄宗" width="100%"></a><br><a href="https://x.com/FiniYang/status/2119583244937314674"><b>懸霄宗</b></a><br><a href="https://x.com/FiniYang">@FiniYang</a> · 提示詞未公開<br><sub>作者自述</sub></td><td width="33%" valign="top"><a href="https://x.com/MKULTRAG0D/status/2119497045052707196"><img src="https://pbs.twimg.com/media/HWn3U9EWcAA-BQK.jpg?name=large" alt="Blender 廢棄屋" width="100%"></a><br><a href="https://x.com/MKULTRAG0D/status/2119497045052707196"><b>Blender 廢棄屋</b></a><br><a href="https://x.com/MKULTRAG0D">@MKULTRAG0D</a> · <a href="prompts/mkultrag0d-707196.md">提示詞</a>（部分）<br><sub>Blender MCP · 作者自述</sub><br><sub>作者說手感好過 6.1，但沒有同一提示詞的對照。</sub></td></tr>
</table>
<a id="cat-character"></a>
## 角色、動態與繪像（9）

<table>
<tr><td width="33%" valign="top"><a href="https://x.com/Ananth7e/status/2119471963790065987"><img src="https://pbs.twimg.com/amplify_video_thumb/2119471570100113408/img/fozT2Bh7cobCx57_.jpg" alt="畫 Sam Altman" width="100%"></a><br><a href="https://x.com/Ananth7e/status/2119471963790065987"><b>畫 Sam Altman</b></a><br><a href="https://x.com/Ananth7e">@Ananth7e</a> · 提示詞未公開<br><sub>作者自述</sub><br><sub>預覽是開始畫面，不是完成品。</sub></td><td width="33%" valign="top"><a href="https://x.com/Mr_Salio/status/2119499550373425297"><img src="https://pbs.twimg.com/amplify_video_thumb/2119499524137697280/img/CDfdmWjfwMiHHKQs.jpg" alt="畫 @thsottiaux" width="100%"></a><br><a href="https://x.com/Mr_Salio/status/2119499550373425297"><b>畫 @thsottiaux</b></a><br><a href="https://x.com/Mr_Salio">@Mr_Salio</a> · 提示詞未公開<br><sub>作者自述</sub><br><sub>預覽是 0 strokes 的起始幀。</sub></td><td width="33%" valign="top"><a href="https://x.com/SahilPanhotra/status/2119453829632868388"><img src="https://pbs.twimg.com/amplify_video_thumb/2119453646454964224/img/iuG6_NdUtqCq8AIS.jpg" alt="孔雀騎 BMX" width="100%"></a><br><a href="https://x.com/SahilPanhotra/status/2119453829632868388"><b>孔雀騎 BMX</b></a><br><a href="https://x.com/SahilPanhotra">@SahilPanhotra</a> · 提示詞未公開<br><sub>作者自述</sub><br><sub>帖文同時引用了他自己更早的 Gemini 測試，那支不是這支 10 秒影片。</sub></td></tr>
<tr><td width="33%" valign="top"><a href="https://x.com/marcthecreatorr/status/2119466616693850352"><img src="https://pbs.twimg.com/media/HWnbpRnW8AAmOqJ.jpg?name=large" alt="Ana de Armas 與 Sam Altman" width="100%"></a><br><a href="https://x.com/marcthecreatorr/status/2119466616693850352"><b>Ana de Armas 與 Sam Altman</b></a><br><a href="https://x.com/marcthecreatorr">@marcthecreatorr</a> · <a href="prompts/marcthecreatorr-850352.md">提示詞</a><br><sub>SVG · 純代碼 · 作者自述</sub></td><td width="33%" valign="top"><a href="https://x.com/xbquan/status/2119479402052657395"><img src="https://pbs.twimg.com/amplify_video_thumb/2119478886493040640/img/V-J4ynpx76jRKOp6.jpg" alt="紫色毛球" width="100%"></a><br><a href="https://x.com/xbquan/status/2119479402052657395"><b>紫色毛球</b></a><br><a href="https://x.com/xbquan">@xbquan</a> · 提示詞未公開<br><sub>作者自述 · 對照 Opus 5.5</sub><br><sub>「秒殺」和「大於 Opus」是作者結論。</sub></td><td width="33%" valign="top"><a href="https://x.com/FiniYang/status/2119474691727671736"><img src="https://pbs.twimg.com/amplify_video_thumb/2119473335822376960/img/gtpUqGnZb3e3xXNQ.jpg" alt="鵜鶘騎車" width="100%"></a><br><a href="https://x.com/FiniYang/status/2119474691727671736"><b>鵜鶘騎車</b></a><br><a href="https://x.com/FiniYang">@FiniYang</a> · 提示詞未公開<br><sub>作者自述</sub></td></tr>
<tr><td width="33%" valign="top"><a href="https://x.com/BreezeOg1/status/2119495488445497489"><img src="https://pbs.twimg.com/media/HWn16HjXQAEJ6jQ.jpg" alt="節拍動態測試" width="100%"></a><br><a href="https://x.com/BreezeOg1/status/2119495488445497489"><b>節拍動態測試</b></a><br><a href="https://x.com/BreezeOg1">@BreezeOg1</a> · 提示詞未公開<br><sub>純代碼 · 作者自述</sub><br><sub>預覽幀是標題卡，成片內容只依作者描述。</sub></td><td width="33%" valign="top"><a href="https://x.com/Mr_Salio/status/2119534613529866398"><img src="https://pbs.twimg.com/amplify_video_thumb/2119534582387154944/img/vrfr7UY079TJPbol.jpg" alt="18 秒的肖像介面" width="100%"></a><br><a href="https://x.com/Mr_Salio/status/2119534613529866398"><b>18 秒的肖像介面</b></a><br><a href="https://x.com/Mr_Salio">@Mr_Salio</a> · 提示詞未公開<br><sub>作者自述</sub><br><sub>預覽是起始幀，不是成稿。</sub></td><td width="33%" valign="top"><a href="https://x.com/FiniYang/status/2119489663971029254"><img src="https://pbs.twimg.com/amplify_video_thumb/2119489544571826176/img/7cxlIUhHAyBILE72.jpg" alt="螺旋多米諾" width="100%"></a><br><a href="https://x.com/FiniYang/status/2119489663971029254"><b>螺旋多米諾</b></a><br><a href="https://x.com/FiniYang">@FiniYang</a> · 提示詞未公開<br><sub>Three.js · 作者自述</sub><br><sub>Three.js 來自預覽幀上的字，不是帖文正文。</sub></td></tr>
</table>
<a id="cat-comparison"></a>
## 對照（10）

<table>
<tr><td width="33%" valign="top"><a href="https://x.com/TokenGremlin/status/2119423600692166703"><img src="https://pbs.twimg.com/amplify_video_thumb/2119423566944854016/img/RX0joNUoH2bqKqYB.jpg" alt="黑洞上下對照" width="100%"></a><br><a href="https://x.com/TokenGremlin/status/2119423600692166703"><b>黑洞上下對照</b></a><br><a href="https://x.com/TokenGremlin">@TokenGremlin</a> · 提示詞未公開<br><sub>Three.js · 作者自述 · 對照 Opus 5.5</sub><br><sub>對照標籤來自作者，不是獨立復現。</sub></td><td width="33%" valign="top"><a href="https://x.com/vikktorrrre/status/2119473712751649201"><img src="https://pbs.twimg.com/amplify_video_thumb/2119473584762396672/img/lnAT6YCtSxqTjDkn.jpg" alt="錦鯉池，時間與費用" width="100%"></a><br><a href="https://x.com/vikktorrrre/status/2119473712751649201"><b>錦鯉池，時間與費用</b></a><br><a href="https://x.com/vikktorrrre">@vikktorrrre</a> · 提示詞未公開<br><sub>作者自述 · 對照 Opus 5.5</sub><br><sub>費用和時間是作者單次測試的自述。</sub></td><td width="33%" valign="top"><a href="https://x.com/HarshithLucky3/status/2119424342773866559"><img src="https://pbs.twimg.com/amplify_video_thumb/2119424200662556672/img/F88nVhePriAP2wcO.jpg" alt="側視奔跑的獵豹" width="100%"></a><br><a href="https://x.com/HarshithLucky3/status/2119424342773866559"><b>側視奔跑的獵豹</b></a><br><a href="https://x.com/HarshithLucky3">@HarshithLucky3</a> · <a href="prompts/harshithlucky3-866559.md">提示詞</a>（部分）<br><sub>作者自述 · 對照 Opus 5.5</sub><br><sub>「遠不如 Opus」是正文判斷，縮圖裡看不見對照組。</sub></td></tr>
<tr><td width="33%" valign="top"><a href="https://x.com/marcthecreatorr/status/2119503438405136765"><img src="https://pbs.twimg.com/amplify_video_thumb/2119502925797953536/img/wiZ1ZbgBM5mZnQY9.jpg" alt="帆船上下對照" width="100%"></a><br><a href="https://x.com/marcthecreatorr/status/2119503438405136765"><b>帆船上下對照</b></a><br><a href="https://x.com/marcthecreatorr">@marcthecreatorr</a> · <a href="prompts/marcthecreatorr-136765.md">提示詞</a>（部分）<br><sub>Three.js · 作者自述 · 對照 Opus 5.5</sub><br><sub>對照標籤和報價都是作者自述。</sub></td><td width="33%" valign="top"><a href="https://x.com/theaidesk_/status/2119516309851361758"><img src="https://pbs.twimg.com/amplify_video_thumb/2119516264280313856/img/8xlt-qeM2WYC_0SC.jpg" alt="白宮場景" width="100%"></a><br><a href="https://x.com/theaidesk_/status/2119516309851361758"><b>白宮場景</b></a><br><a href="https://x.com/theaidesk_">@theaidesk_</a> · 提示詞未公開<br><sub>作者自述 · 對照 Qwen</sub><br><sub>作者只說可能是 gpt-6.2 sol。</sub></td><td width="33%" valign="top"><a href="https://x.com/theaidesk_/status/2119503807654535300"><img src="https://pbs.twimg.com/amplify_video_thumb/2119503448211091456/img/-0HNzwnUKr8Rwfh6.jpg" alt="夜間教堂，兩支影片" width="100%"></a><br><a href="https://x.com/theaidesk_/status/2119503807654535300"><b>夜間教堂，兩支影片</b></a><br><a href="https://x.com/theaidesk_">@theaidesk_</a> · 提示詞未公開<br><sub>作者自述 · 對照 Opus 5.5</sub><br><sub>作者用了 possibly，沒有把 6.2 Sol 說死。</sub></td></tr>
<tr><td width="33%" valign="top"><a href="https://x.com/AnikaCodes/status/2119469611473358879"><img src="https://pbs.twimg.com/amplify_video_thumb/2119458208041574400/img/Bd6ESUNUIcU-hf0L.jpg" alt="騎車的獅子" width="100%"></a><br><a href="https://x.com/AnikaCodes/status/2119469611473358879"><b>騎車的獅子</b></a><br><a href="https://x.com/AnikaCodes">@AnikaCodes</a> · 提示詞未公開<br><sub>作者自述 · 對照 GPT-6.1 Sol</sub><br><sub>前後差異被作者歸因於路由，本庫沒有復現昨天那一版。</sub></td><td width="33%" valign="top"><a href="https://x.com/AnikaCodes/status/2119435328503308608"><img src="https://pbs.twimg.com/media/HWmux-bW4AAK2Wz.jpg?name=large" alt="遊戲手把" width="100%"></a><br><a href="https://x.com/AnikaCodes/status/2119435328503308608"><b>遊戲手把</b></a><br><a href="https://x.com/AnikaCodes">@AnikaCodes</a> · 提示詞未公開<br><sub>作者自述 · 對照 GPT-6.1 Sol</sub><br><sub>畫面水印是另一位作者。</sub></td><td width="33%" valign="top"><a href="https://x.com/xbquan/status/2119581984989364514"><img src="https://pbs.twimg.com/media/HWpDiiLaQAAuBnd.jpg?name=large" alt="孫悟空大鬧天宮" width="100%"></a><br><a href="https://x.com/xbquan/status/2119581984989364514"><b>孫悟空大鬧天宮</b></a><br><a href="https://x.com/xbquan">@xbquan</a> · 提示詞未公開<br><sub>SVG · 作者自述 · 對照 Qoder Qoduck / WorkBuddy hy4</sub><br><sub>這是多模型對照，不是和 Opus 的對照。</sub></td></tr>
<tr><td width="33%" valign="top"><a href="https://x.com/surfing_fatcat/status/2119462600375402911"><img src="https://pbs.twimg.com/amplify_video_thumb/2119462471249670144/img/QNkzd96RznmUcDZr.jpg" alt="星際穿越風黑洞與風暴船" width="100%"></a><br><a href="https://x.com/surfing_fatcat/status/2119462600375402911"><b>星際穿越風黑洞與風暴船</b></a><br><a href="https://x.com/surfing_fatcat">@surfing_fatcat</a> · 提示詞未公開<br><sub>Three.js · 單檔 HTML · 作者自述 · 對照 Opus 5.5 / GPT-6 Astra</sub><br><sub>檢測問句與作品是兩件事。</sub></td></tr>
</table>

<a id="how-to-use"></a>
## 提示詞怎麼用

公開原文只有這 5 份：

- [時間的盡頭](prompts/khazix0918-144677.md) · [@Khazix0918](https://x.com/Khazix0918/status/2119507514459144677) · 全文
- [Ana de Armas 與 Sam Altman](prompts/marcthecreatorr-850352.md) · [@marcthecreatorr](https://x.com/marcthecreatorr/status/2119466616693850352) · 全文
- [側視奔跑的獵豹](prompts/harshithlucky3-866559.md) · [@HarshithLucky3](https://x.com/HarshithLucky3/status/2119424342773866559) · 部分
- [帆船上下對照](prompts/marcthecreatorr-136765.md) · [@marcthecreatorr](https://x.com/marcthecreatorr/status/2119503438405136765) · 部分
- [Blender 廢棄屋](prompts/mkultrag0d-707196.md) · [@MKULTRAG0D](https://x.com/MKULTRAG0D/status/2119497045052707196) · 部分

1. 打開提示詞檔，複製 **Prompt** 區塊。沒有檔的條目就是沒有公開全文，不要把標題、縮圖或本庫的說明當成提示詞。
2. 貼到你自己的程式代理。作者多半是在說 ChatGPT 或 Codex 裡被路由之後的結果，你不一定走同一條路由。
3. 原作若是 Three.js、SVG 或單檔網頁，請它交付一個 HTML，再用瀏覽器打開。
4. 標成部分的提示詞不要預期相同畫面。廢棄屋那一份還依賴帖裡的參考圖，圖不在本庫。
5. 不要用 Tony Awards、Fable 5、Karpathy 在 2026 年 5 月這類知識截止題來判斷模型。@notjazii 已寫明 6.1 的 API 知道 Tony 那一題。用量頁出現 `gpt-6.2-sol` 字串也只是使用者貼出的線索，不是官宣。

<a id="context"></a>
## 脈絡，不計入畫廊

下面 57 則都在種子 91 篇裡，有原帖連結，但**不計入畫廊**。檢測題保留下來，是為了讓反證和衝突說法跟作品分開，不是推薦那些問法。

<details>
<summary>官方帖，不是模型發布（1，不計入畫廊）</summary>

| 時間 | 作者 | 原帖 | 說明 |
| --- | --- | --- | --- |
| 2026-11-09 04:04:05 | [@OpenAIDevs](https://x.com/OpenAIDevs) | [帖](https://x.com/OpenAIDevs/status/2119521359185478140) | 官方開發者帳只寫「Tomorrow.」並附影片；社群大量聯想 GPT-6.2 Sol，但 Grok 回覆指出內容實為 OpenAI×ModRetro Chromatic 掌機 11/9 上架預告，並非官宣 6.2 Sol。 核對：帖文只有 Tomorrow.。公開預覽幀是復古像素字 CONTINUE，不是模型演示。種子彙整認為這是掌機預告；這一幀本身沒有寫出產品名。 |

</details>
<details>
<summary>路由檢測與反證（14，不計入畫廊）</summary>

| 時間 | 作者 | 原帖 | 說明 |
| --- | --- | --- | --- |
| 2026-11-08 19:32:52 | [@N1n3VASthR33H](https://x.com/N1n3VASthR33H) | [帖](https://x.com/N1n3VASthR33H/status/2119392706644566435) | 中文檢測：Codex/Work 選 xhigh，問「已發生且最接近2027年的事」；若回五月後事件則視為灰度。並提 Opus/Astra6.2/Sol6.2 盲測連結。 |
| 2026-11-08 22:53:06 | [@AGTPinsights](https://x.com/AGTPinsights) | [帖](https://x.com/AGTPinsights/status/2119443099478831550) | 新聞式整理：路由報告、Fable5 檢測法、延遲背景、懷疑聲音與數字摘錄；並明寫 OpenAI 尚未官宣 6.2 Sol／Astra。 |
| 2026-11-08 23:35:30 | [@AiBattle_](https://x.com/AiBattle_) | [帖](https://x.com/AiBattle_/status/2119453769989517629) | 偵測方法：問「who hosted the Tony Awards (June 7, 2026)? no web search」，正確應答 P!nk 則可能已被路由到 6.2 Sol。有反證：@notjazii（https://x.com/notjazii/status/2119515293622083816）指出 6.1 API 已知此題，不能單憑此題確認模型；該用戶並改推 Fable 5／Tibo／Karpathy May 2026（禁搜），且自稱已路由、模型大幅強於 6.1——用戶聲稱，未獨立驗證。 核對：這是 Tony Awards 檢測題，不是視覺作品。@notjazii 指出 6.1 API 已經知道這題，不能單憑答對確認模型。 |
| 2026-11-08 23:49:31 | [@FiniYang](https://x.com/FiniYang) | [帖](https://x.com/FiniYang/status/2119457294715068928) | 自稱再次灰度；檢測：選 GPT-6.1 Sol Max，問「do you know Fable 5 (no web search)」。 |
| 2026-11-09 00:35:57 | [@Mr_Salio](https://x.com/Mr_Salio) | [帖](https://x.com/Mr_Salio/status/2119468979559313865) | 檢測證據帖：對 6.1 Sol Max 問「do you know fable 5 no web search」若能答則自稱被路由到新模型；附影片證明。用戶側灰度檢測法。 核對：短片用來展示 Fable 5 問句，不是視覺演示。 |
| 2026-11-09 01:06:06 | [@dedene](https://x.com/dedene) | [帖](https://x.com/dedene/status/2119476570058330498) | 自測 Tony Awards 題答 P!nk，懷疑已被路由。註：Tony Awards 單題有反證（6.1 API 已知），不能單憑此題確認模型；用戶側判定未獨立驗證。 |
| 2026-11-09 02:51:36 | [@notjazii](https://x.com/notjazii) | [帖](https://x.com/notjazii/status/2119503117603713110) | Codex 自測：跑提示後模型兩邊知識都知道，自問是否已被 6.1→6.2 路由；附截圖。用戶側判定。 |
| 2026-11-09 03:28:35 | [@SergioGMN](https://x.com/SergioGMN) | [帖](https://x.com/SergioGMN/status/2119512426110742533) | 西語轉述路由＋Tony Awards／P!nk 檢測題。註：Tony Awards 單題有反證（6.1 API 已知），不能單憑此題確認模型；用戶側判定未獨立驗證。 |
| 2026-11-09 03:39:59 | [@notjazii](https://x.com/notjazii) | [帖](https://x.com/notjazii/status/2119515293622083816) | 指出 Tony Awards 檢測題可能誤判：稱 6.1 API 已知此題，不能單憑答對確認路由到 6.2；改推三題（禁搜）：Fable 5／Tibo／Karpathy May 2026。並自稱已被路由且輸出大幅強於 6.1——用戶側判定，未獨立驗證。 核對：反證帖：作者稱 6.1 API 已知 Tony 題，並改推 Fable 5、Tibo、Karpathy 2026 年 5 月三題。這些仍是知識截止題，不是充分條件，也不是作品提示詞。 |
| 2026-11-09 07:35:00 | [@TylerBai_loveai](https://x.com/TylerBai_loveai) | [帖](https://x.com/TylerBai_loveai/status/2119574437104345277) | 同 Fable5 檢測法；作者稱自己 Plus 手機端 Codex 雲端未中灰度。 |
| 2026-11-09 07:51:22 | [@JuanByteLabs](https://x.com/JuanByteLabs) | [帖](https://x.com/JuanByteLabs/status/2119578557873791409) | Tony Awards 檢測僅在 Web Work＋Xhigh 生效；同 prompt Max 不知——附圖對照。註：Tony Awards 單題有反證（6.1 API 已知），不能單憑此題確認模型；用戶側判定未獨立驗證。 |
| 2026-11-09 08:00:00 | [@julsix2333](https://x.com/julsix2333) | [帖](https://x.com/julsix2333/status/2119580731274088920) | Codex 切 gpt-6.1-sol xhigh，問離2027最近已發生之事；若回2026年5月後則中獎。 |
| 2026-11-09 08:09:23 | [@xluchuan](https://x.com/xluchuan) | [帖](https://x.com/xluchuan/status/2119583091341799526) | 檢測：禁止聯網問「你知道 Fable 5 嗎」，知道則訓練截止較晚、可能灰度。 |
| 2026-11-09 08:48:14 | [@theolearnsAI](https://x.com/theolearnsAI) | [帖](https://x.com/theolearnsAI/status/2119592868621029460) | 【08:40後新帖】檢測法補充：界面仍顯示 6.1 Sol，但用量頁可出現 gpt-6.2-sol；強調非官宣、公開目錄無正式 6.2。曝光極低但方法新。 核對：作者說介面仍顯示 6.1，用量頁可能出現字串 gpt-6.2-sol，並強調這不是官宣。這是使用者觀察，不是模型鑑定，也沒有作品畫面。 |

</details>
<details>
<summary>轉載、轉述與衝突歸因（19，不計入畫廊）</summary>

| 時間 | 作者 | 原帖 | 說明 |
| --- | --- | --- | --- |
| 2026-11-08 19:52:54 | [@adityaa_behera](https://x.com/adityaa_behera) | [帖](https://x.com/adityaa_behera/status/2119397747124252806) | 早期放大 TokenGremlin 黑洞：強調 one-shot、Three.js、單 HTML、早期測試勝過 Opus 5.5。用戶側轉述。 核對：沒有自己的新畫面，轉述 TokenGremlin 的黑洞帖。 |
| 2026-11-08 20:40:43 | [@kimmonismus](https://x.com/kimmonismus) | [帖](https://x.com/kimmonismus/status/2119409780691284404) | 觀察多地用戶被路由；推測下周為發布週；引用 TokenGremlin 輸出。 核對：引用 TokenGremlin 的輸出，自己沒有另附作品。 |
| 2026-11-08 20:57:18 | [@Smlay_ero](https://x.com/Smlay_ero) | [帖](https://x.com/Smlay_ero/status/2119413954950914258) | 轉述路由實測：one-shot、Three.js、單 HTML；稱測評勝過 Opus 5.5。 核對：沒有自己的新畫面，轉述同一則 Three.js 演示。 |
| 2026-11-08 21:27:20 | [@SiftByte](https://x.com/SiftByte) | [帖](https://x.com/SiftByte/status/2119421515464921360) | 並列影片：自稱第一支為路由 GPT-6.2 Sol、另一支 Opus 5.5；稱能力大致持平，並預測 Astra≈Fable 5.5。用戶側判定。 核對：第一支媒體與 @JangXiin 的帖相同，該帖寫的是 Opus 5.5 one-shot。第二支與 @TokenGremlin 自稱為 Sol 的黑洞相同。這則卻寫「第一支是 Sol、另一支是 Opus」，和兩邊原帖相反，所以不進畫廊。 |
| 2026-11-08 21:33:24 | [@daniel_mac8](https://x.com/daniel_mac8) | [帖](https://x.com/daniel_mac8/status/2119423039678910754) | 預測：Sol 11/9 發、優於 Opus 5.5；Astra 11/12、對齊 Fable 5.5；更省約50%。非實測，屬預測帖。 核對：正文寫預測，並註明影片來自 @TokenGremlin。媒體與黑洞原帖相同，不另計。 |
| 2026-11-08 21:35:52 | [@Super_Nius](https://x.com/Super_Nius) | [帖](https://x.com/Super_Nius/status/2119423660381610370) | 灰測前端能力升級，稱接近 Opus 5.5，並強調仍只是 Sol 非 Astra。 核對：所附影片和圖片與 TokenGremlin 的黑洞帖是同一組媒體。 |
| 2026-11-08 22:13:29 | [@ai_funss](https://x.com/ai_funss) | [帖](https://x.com/ai_funss/status/2119433127810777099) | 灰度檢測：選 6.1 Sol Max，問「do you know Fable 5 (no web search)」；並稱 3D 效果強。 核對：圖片是 TokenGremlin 黑洞的靜幀。正文是 Fable 5 檢測法，不是新的 3D 作品。 |
| 2026-11-08 22:29:30 | [@leo114119](https://x.com/leo114119) | [帖](https://x.com/leo114119/status/2119437157068890174) | 黑洞模擬對比：感覺 Sol 略優於 Opus 5.5。 核對：影片與 TokenGremlin 標成 Sol／Opus 的黑洞對照是同一支。這裡是轉述，不是新測試。 |
| 2026-11-09 02:30:17 | [@xingzengji](https://x.com/xingzengji) | [帖](https://x.com/xingzengji/status/2119497752325611587) | 轉述同 prompt 成本對比：Sol ~20分/$9 vs Opus ~1h/$20。 核對：轉述 20 分鐘／9 美元對 1 小時／20 美元。影片時長與尺寸和 @vikktorrrre 的錦鯉池對照一致，縮圖 id 不同，沒有看到獨立的新測試。 |
| 2026-11-09 02:59:38 | [@CranelAnos](https://x.com/CranelAnos) | [帖](https://x.com/CranelAnos/status/2119505138696298860) | 轉述／加碼 marcthecreatorr 帆船 Three.js 對比：稱 Sol 畫面整體更好、Opus 霸權結束中；並問能否扛住 Opus Next。 核對：帆船影片與 @marcthecreatorr 的對照相同，帖文也寫了出處。 |
| 2026-11-09 03:20:35 | [@Super_Nius](https://x.com/Super_Nius) | [帖](https://x.com/Super_Nius/status/2119510410751795268) | 中文對比轉述：左 Opus 5.5／右自稱 GPT-6.2 Sol 的四場景 SVG（月球站、咖啡機、唱機、溫室）；稱 Sol 更暖更滿料。來源轉引社群對比影片。 核對：影片與 @Ananth7e 的「Opus 5.5 vs GPT-6.2 Sol: animated SVGs」是同一支。該預覽的左欄小字寫 Archived footage、Original video labeled Opus 5.2，右欄小字寫 SVGs generated with GPT-6.1 Sol，和標題上的 5.5／6.2 衝突。底部有一小段提示詞，字級不足以逐字抄錄，因此不收入 prompts/。不計入畫廊。 |
| 2026-11-09 04:15:38 | [@JotaroKujoX](https://x.com/JotaroKujoX) | [帖](https://x.com/JotaroKujoX/status/2119524264890007772) | 聚焦帳單：轉述帆船測 Sol ~27分/$3 vs Opus ~1h35/$16；提醒單次測試＋未官宣。 核對：討論帆船測試的帳單，引用 @marcthecreatorr，沒有自己的新畫面。 |
| 2026-11-09 06:46:31 | [@RJasonHA](https://x.com/RJasonHA) | [帖](https://x.com/RJasonHA/status/2119562236347961758) | 彙整前端／3D 反饋＋自測步驟：選 6.1 Sol Max/xhigh，關聯網與記憶，丟檢測題。 核對：彙整檢測步驟，影片指向 @Mr_Salio 的浮島原帖，不是新作品。檢測步驟不能確認模型。 |
| 2026-11-09 07:40:00 | [@JamesDa55049936](https://x.com/JamesDa55049936) | [帖](https://x.com/JamesDa55049936/status/2119575695282327559) | 轉述 Plus 連續 ~4.5h Three.js／設計／寫碼才撞限——額度放寬敘事。 核對：轉述 Plus 連續使用約 4.5 小時才撞限，圖是用量截圖，不是作品。 |
| 2026-11-09 07:46:32 | [@xKaka1456](https://x.com/xKaka1456) | [帖](https://x.com/xKaka1456/status/2119577342054170709) | 轉述對比數字：Sol 20分鐘/$9 vs Opus 60分鐘/$20（與 vikk 帖一致口徑）。 核對：影片與 @vikktorrrre 的錦鯉池對照是同一支媒體。 |
| 2026-11-09 07:52:00 | [@cfenghub](https://x.com/cfenghub) | [帖](https://x.com/cfenghub/status/2119578715399327947) | 轉述 Three.js 單 HTML 村莊實測：零外部資產、晝夜光影；強調價格與性能敘事。 核對：轉述村莊演示。影片與 @TokenGremlin 的櫻花村莊原帖相同，畫廊已改記原帖。 |
| 2026-11-09 08:00:02 | [@ChrisHKAI](https://x.com/ChrisHKAI) | [帖](https://x.com/ChrisHKAI/status/2119580736315342972) | 用 Sam Altman 主題測試 GPT-6.2 Sol。 核對：影片與 @Ananth7e「paints sam altman」是同一支媒體。 |
| 2026-11-09 08:30:00 | [@ChrisHKAI](https://x.com/ChrisHKAI) | [帖](https://x.com/ChrisHKAI/status/2119588278232109363) | 轉述卡茲克灰度；複用《時間的盡頭》Three.js prompt，感覺比 Astra 強。 核對：影片和《時間的盡頭》提示詞都與 @Khazix0918 原帖相同，不另建提示詞檔。 |
| 2026-11-09 08:45:09 | [@yulmu_coffee](https://x.com/yulmu_coffee) | [帖](https://x.com/yulmu_coffee/status/2119592091785535536) | 【08:40後新帖】韓文：自稱 GPT-6.2 Sol computer-use 畫 Sam Altman 的 time-lapse 影片。用戶側演示；曝光尚低。 核對：開頭幀與 @Ananth7e 畫 Sam Altman 幾乎同一格（色號 #42372d、同一張參考照、825×875、Block-in），多了一支紅箭頭。時長 316.8 秒，媒體 id 不同，但不能當成第二件已核實的獨立作品。 |

</details>
<details>
<summary>意見與額度（10，不計入畫廊）</summary>

| 時間 | 作者 | 原帖 | 說明 |
| --- | --- | --- | --- |
| 2026-11-08 22:45:11 | [@ai_funss](https://x.com/ai_funss) | [帖](https://x.com/ai_funss/status/2119441107205718464) | 測評向：灰度到 6.2 Sol 後「防御性回复」改善——不再動輒「不能確定／不證明」。 核對：正文在談防禦性回覆變少。所附圖片是知識截止問答，介面標 GPT-6.1 Sol 極高，不是生成畫面。 |
| 2026-11-09 00:02:48 | [@HarshithLucky3](https://x.com/HarshithLucky3) | [帖](https://x.com/HarshithLucky3/status/2119460639345369425) | 反方：Opus 5.5 >>> GPT 6.2 Sol（並預判會被質疑「你沒路由到」）。 |
| 2026-11-09 00:08:31 | [@TokenGremlin](https://x.com/TokenGremlin) | [帖](https://x.com/TokenGremlin/status/2119462074971480136) | 短評「GPT-6.2 Sol > Opus 5.5」，引發大量引用／對比測試。 |
| 2026-11-09 02:02:17 | [@TokenGremlin](https://x.com/TokenGremlin) | [帖](https://x.com/TokenGremlin/status/2119490708876955697) | 個人測評長文：遠超 6.1 Sol、設計口味優於 Opus 5.5、比 Max 下 Astra 更好；數十次 Three.js/WebGPU 測試僅耗約 10% 的 $200 Pro 額度；期待 Plus 也有寬裕用量。 |
| 2026-11-09 02:59:14 | [@TimJayas](https://x.com/TimJayas) | [帖](https://x.com/TimJayas/status/2119505038246916496) | 反方觀點：多數 6.2 Sol 帖是誇大；未見 6.2 能做而 6.1 不能的事；.1 升級難合理化「大幅勝過 Opus 5.5」。 |
| 2026-11-09 03:39:24 | [@Mr_Salio](https://x.com/Mr_Salio) | [帖](https://x.com/Mr_Salio/status/2119515145382633524) | Plus $20：6.1 Max 路由到 6.2 Sol 連續跑約4.5小時才撞限；多個 Three.js／網頁設計／編程實驗。 核對：圖片是 Work 用量用盡的對話框，不是 Three.js 作品。 |
| 2026-11-09 06:00:56 | [@TJeparskis](https://x.com/TJeparskis) | [帖](https://x.com/TJeparskis/status/2119550763491897758) | 額度觀察：全日幾乎不間斷仍未撞 5 小時限額，懷疑被路由到 6.2 Sol；預測 Sol 週二、Astra 週四交錯發布。官方未確認。 |
| 2026-11-09 07:21:59 | [@ThanksuTrump](https://x.com/ThanksuTrump) | [帖](https://x.com/ThanksuTrump/status/2119571164116972024) | 轉述卡茲克向：並發20前端測10分鐘，$200 Pro 額度只掉1%；審美與防禦改善。 核對：主旨是 200 美元額度只掉 1%。截圖裡有山水成片，但介面標 GPT-6.1 Sol Max，不把這張工作階段截圖算成 6.2 畫廊作品。 |
| 2026-11-09 07:37:28 | [@YFeng2022](https://x.com/YFeng2022) | [帖](https://x.com/YFeng2022/status/2119575058305753202) | 質疑：如何判定真是 6.2 Sol？覺得表演成分重。 |
| 2026-11-09 08:25:16 | [@argofowl](https://x.com/argofowl) | [帖](https://x.com/argofowl/status/2119587087771185405) | 引用 vikktorrrre 對比帖反駁：1) Opus 5.5 更好；2) 那不是 gpt sol 6.2。用戶側反方判定。 |

</details>
<details>
<summary>發布傳聞與跟風（13，不計入畫廊）</summary>

| 時間 | 作者 | 原帖 | 說明 |
| --- | --- | --- | --- |
| 2026-11-09 01:35:27 | [@dummerspast39](https://x.com/dummerspast39) | [帖](https://x.com/dummerspast39/status/2119483953354842554) | 用戶側傳聞：內線稱 GPT-6.2 Sol 下週四發布、Codex 已有人用到；並稱會贏 Opus 5.5 且成本約三分之一，Astra 因安全問題稍晚。官方未確認；與「Tomorrow.」是否同一事仍不明。 |
| 2026-11-09 03:02:25 | [@TokenGremlin](https://x.com/TokenGremlin) | [帖](https://x.com/TokenGremlin/status/2119505841883640170) | TokenGremlin 傳聞：Anthropic 本週可能連發安全／對齊／節奏相關部落格，以對衝 GPT-6.2 Astra／Sol。官方未確認。 |
| 2026-11-09 03:55:15 | [@jessexai_](https://x.com/jessexai_) | [帖](https://x.com/jessexai_/status/2119519134182494562) | 傳聞：Anthropic 會在 OpenAI 週四發 GPT-6.2 Sol 後 30 分鐘丟 Fable 5.5。官方未確認；與 dummerspast 週四說呼應。 |
| 2026-11-09 06:48:13 | [@Policifyai](https://x.com/Policifyai) | [帖](https://x.com/Policifyai/status/2119562665899262373) | 周末「掉落」盤點：6.2 Sol「部分用戶路由、無人正式確認」；今日能用模型仍同週五。 |
| 2026-11-09 08:25:00 | [@duoyun_77](https://x.com/duoyun_77) | [帖](https://x.com/duoyun_77/status/2119587019978396086) | 爆料敘事（引用舊預測帖）：下週四 11/12 發布＋Codex 已可用＋比 Opus 更強更便宜；附跑分／價格截圖，仍自標爆料。 |
| 2026-11-09 08:36:58 | [@wellzhiai](https://x.com/wellzhiai) | [帖](https://x.com/wellzhiai/status/2119590031748890912) | 【近窗】引用 OpenAIDevs「Tomorrow.」猜測「明天發 GPT 6.2 Astra」——誤聯想標註：該官帖多為 Chromatic 掌機預告，非模型官宣。 |
| 2026-11-09 08:41:07 | [@SeiraHisada](https://x.com/SeiraHisada) | [帖](https://x.com/SeiraHisada/status/2119591077372174835) | 日文 AI 早刊：頂條 OpenAIDevs「Tomorrow.」＋社群 Three.js／6.2 Sol 路由報告。 |
| 2026-11-09 08:42:19 | [@Junp_Li](https://x.com/Junp_Li) | [帖](https://x.com/Junp_Li/status/2119591380167340047) | 評論 Tomorrow. 與滿屏灰度測試，問能否拉下 Opus 5.5。 |
| 2026-11-09 08:43:33 | [@jamisafari](https://x.com/jamisafari) | [帖](https://x.com/jamisafari/status/2119591691351126037) | 【08:40後新帖】科普向日報把 OpenAIDevs「Tomorrow.」與「已有人拿到 GPT-6.2 Sol」並列；易誤聯想為模型官宣（實為 Chromatic 掌機預告已入庫）。 |
| 2026-11-09 08:44:05 | [@_jayyy18_13k](https://x.com/_jayyy18_13k) | [帖](https://x.com/_jayyy18_13k/status/2119591822930714837) | 詢問他人是否已拿到 GPT-6.2 Sol 存取。 |
| 2026-11-09 08:48:03 | [@xun403](https://x.com/xun403) | [帖](https://x.com/xun403/status/2119592823838396497) | 自稱也被路由到 GPT-6.2 Sol（附圖）。 核對：使用者自稱路由到 6.2，截圖介面仍標 GPT-6.1 Sol Max，內容是 Fable 問答。 |
| 2026-11-09 08:48:42 | [@TheEaglegon](https://x.com/TheEaglegon) | [帖](https://x.com/TheEaglegon/status/2119592983729508716) | 回覆額度討論：若 6.2 Sol 更省額度，5 小時上限就不綁；推測 Sol 週二／Astra 週四，但 Tomorrow. 可能只對應一則官宣。 |
| 2026-11-09 08:50:28 | [@migrant2029](https://x.com/migrant2029) | [帖](https://x.com/migrant2029/status/2119593430481596552) | 附圖自問「這算灰度到 gpt 6.2 sol 了嗎」——用戶側判定截圖。 核對：截圖裡模型回答目前記錄是 gpt-6.1-sol。這和「是不是 6.2」衝突，只可當使用者貼出的對話，不是作品。 |

</details>

<a id="excluded"></a>
## 已排除

1 則與這次 6.2 Sol 討論不是同一件事，連脈絡表也不放。

| 時間 | 作者 | 原帖 | 說明 |
| --- | --- | --- | --- |
| 2026-11-09 08:09:01 | [@zshjzls](https://x.com/zshjzls) | [帖](https://x.com/zshjzls/status/2119583000337785039) | 【非6.2 Sol】提 OpenAI LifeVal 基準：GPT-6 Astra 80.6% vs 一年前 GPT-5.2 49.3%。屬舊模型對照，非本次灰度話題。 |

<a id="credits"></a>
## 授權與出處

畫面、提示詞和帖文歸原作者。MIT 只涵蓋這份清單自己的整理、結構和 [`scripts/validate.py`](scripts/validate.py)。完整說明在 [LICENSE](LICENSE)。

分區方式（畫廊、原帖連結、提示詞檔、使用步驟）參考 [yihui-dev/awesome-opus5-5-videos](https://github.com/yihui-dev/awesome-opus5-5-videos)（MIT）。本庫沒有重製網站，也不托管別人的影片。

要改一條或撤下自己的作品，請看 [CONTRIBUTING.md](CONTRIBUTING.md) 並開 issue。

核對方式：91 篇種子帖都用公開帖面讀過正文和媒體類型；畫廊預覽幀有逐張看過的，在 `preview_frame_reviewed` 標成 true。沒有下載完整影片，也沒有把看不見的畫面寫成已經看過。
