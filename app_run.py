from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,ImageSendMessage,VideoSendMessage,FollowEvent
)

import json

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
    userid = json.loads(json.dumps(event.source))['userId']
    line_bot_api.push_message(userid, "fuck", timeout=None)
    curMessage = event.message.text
    if "idiot" in curMessage:
        line_bot_api.reply_message(
        event.reply_token,
        ImageSendMessage(
            original_content_url='https://i.ytimg.com/vi/oujA4rk2s3Q/maxresdefault.jpg',
            preview_image_url='https://i.ytimg.com/vi/oujA4rk2s3Q/maxresdefault.jpg'
        ))
    elif "Nvidia" in curMessage:
        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(
                original_content_url='https://scontent-tpe1-1.xx.fbcdn.net/v/t1.0-9/19400027_10155616239051564_8978737683901429880_n.jpg?oh=d6ead0d58f3359369b39cb50b4ee8ee7&oe=59CB836D', 
                preview_image_url='https://scontent-tpe1-1.xx.fbcdn.net/v/t1.0-9/19400027_10155616239051564_8978737683901429880_n.jpg?oh=d6ead0d58f3359369b39cb50b4ee8ee7&oe=59CB836D'
            ))
    elif curMessage == "!writerwriter":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='https://www.youtube.com/embed/VQ6ch8Brpg4'))
    else :
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=curMessage))

if __name__ == "__main__":
    app.run()