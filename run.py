import os

from flask import Flask, request
from project.services import TelegramWebHookService, LotteryService


def create_chatbot():
    app = Flask(__name__)
    webHookService = TelegramWebHookService()

    @app.route('/')
    def salute():
        return 'Hello, World!'

    @app.route('/', methods=['POST'])
    def start():
        awarded_numbers = LotteryService.summary()

        webHookService.send_message(awarded_numbers)

        return awarded_numbers

    return app


app = create_chatbot()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
