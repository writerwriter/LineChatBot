from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('8jcGFCz9Go0qoKbsILVbhIJdEWGReHqed41Q9xbl/vwNwuppb9rnFFrPURRC1SjZASRIwaxuUVGlMevPEyvzNKsoJ2siWkyp06v2w9IrPRMtd5hnkROuruAQSXgGou7Re3r5LI9DToqEW5rAOMejMAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('98d7239e53dba377e08cd9d1e45f60bb')


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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()