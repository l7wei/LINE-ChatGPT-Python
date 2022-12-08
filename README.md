# LINE-ChatGPT-Python
Use google colab and ngrok to create a line bot communicate with OpenGPT
## 簡介
這個專案是一個聊天機器人，它使用 LINE messaging API 來與使用者互動。
它會聽取來自 /callback 的 Post Request，並且當使用者發送文字訊息給機器人時，會使用 revChatGPT 套件來產生回應，最後再使用 LINE messaging API 將回應傳送給使用者。
它還使用了 Flask 套件來建立 web 應用程式，並且透過 ngrok 套件來建立一個隧道，讓 LINE messaging platform 能夠與聊天機器人通訊。
在執行程式碼時，它會啟動 Flask app 和 ngrok，並且輸出一個可以用來存取 app 的 URL。如果 ngrok 隧道重新啟動，這個 URL 會自動更新。
要使用這個聊天機器人，你需要從 LINE Developers 網站取得自己的 LINE channel access token 和 channel secret，並且在程式碼中替換掉原本的占位符。
## 安裝需求
Python 3
Flask
LINE messaging API 相關函式庫
revChatGPT 套件
ngrok (可選)
## 使用方法
1. 在 LINE Developers 網站取得自己的 LINE channel access token 和 channel secret，並將它們替換到程式碼中的相應位置。
2. 請透過 chat.openai.com 取得 session cookie，並將它替換到程式碼中的相應位置。
3. 安裝所需套件，如果你想使用 ngrok，也請一併安裝。
3. 執行程式碼，它會啟動 Flask app 並輸出一個 URL。
4. 使用瀏覽器存取輸出的 URL，並透過 LINE messaging platform 與聊天機器人互動。
## 備註
如果你使用 ngrok，輸出的 URL 會在 ngrok 隧道重新啟動時自動更新。
如果你想修改機器人的回應方式，可以修改 revChatGPT 套件的參數設定。
如果你想使用 openai.Completion API 來產生回應，請將程式碼中的 openai.Completion.create() 函式的程式碼取消註解。