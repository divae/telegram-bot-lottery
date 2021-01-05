import os

from flask import Flask, request
from project.services import TelegramMessageService, LotteryService


def create_chatbot():
    app = Flask(__name__)

    @app.route('/')
    def salute():
        return 'Hello, World!'

    @app.route('/', methods=['POST'])
    def start():

        awarded_numbers = LotteryService.summary()

        telegram_message_service = TelegramMessageService(request)
        telegram_message_service.change_message(awarded_numbers)
        telegram_message_service.send()

        return awarded_numbers

    return app


app = create_chatbot()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
