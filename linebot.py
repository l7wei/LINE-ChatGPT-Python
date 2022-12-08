from flask import Flask, request

#待官方 API  出來前暫時棄用
#import openai
#openai.api_key = "_____YOUR_OPENAI_API_KEY_____"

# 載入 LINE Message API 相關函式庫
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from flask_ngrok import run_with_ngrok
# 新增 TOKEN 進去
line_bot_api = LineBotApi('_____YOUR_CHANNEL_ACCESS_TOKEN_____')
handler = WebhookHandler('_____YOUR_CHANNEL_SECRET_____')

from revChatGPT.revChatGPT import Chatbot
# https://github.com/acheong08/ChatGPT/wiki/Setup
config = {
    #"email": "<YOUR_EMAIL>",
    #"password": "<YOUR_PASSWORD>"#,
    #"session_token": "<YOUR_SESSION_TOKEN>", # Deprecated. Use only if you encounter captcha with email/password
    #"proxy": "<HTTP/HTTPS_PROXY>"
}
chatbot = Chatbot(config, conversation_id=None)


app = Flask(__name__)
run_with_ngrok(app)   #starts ngrok when the app is run
@app.route("/")
def home():
    return "<h1>Running Flask on Google Colab!</h1>"
# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # Get user's message
    user_message = event.message.text
    '''
    # Use official openai api to generate response
    response = openai.Completion.create(
        engine="text-davinci-003",
        max_tokens=1024,
        n=1,
        temperature=0.9,
    )
    '''
    print(user_message)
    response = chatbot.get_chat_response((user_message), output="text")
    print(response) 
    # Get opengpt's response
    openai_response = response["message"]
    # Send response to user
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=openai_response)
    )

if __name__ == "__main__":
  app.run()