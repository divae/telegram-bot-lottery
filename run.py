import os

from flask import Flask, request
from project.services import TelegramWebHookService


def create_chatbot():
    app = Flask(__name__)
    webHookService = TelegramWebHookService()

    @app.route('/')
    def salute():
        return 'Hello, World!'

    @app.route('/', methods=['POST'])
    def start():
        message = webHookService.process(request)
        webHookService.send_message(message)
        return message

    return app


app = create_chatbot()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
