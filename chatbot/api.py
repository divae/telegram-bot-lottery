from flask import Flask, request

from chatbot.services import LotteryService, TelegramMessageService


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
