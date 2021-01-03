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
        return webHookService.process(request)

    return app

app = create_chatbot()
