import os
import requests
from flask import json


class TelegramMessageService:

    def __init__(self, request):
        request_message = request.get_json()
        self.chat_id = request_message['message']['chat']['id']
        self.text = request_message['message']['text']

    @property
    def message(self):
        return {
            "chat_id": self.chat_id,
            "text": self.text,
        }

    def change_message(self, text):
        self.text = text

    def process(self):
        return self.message

    def send(self):
        TELEGRAM_WEBHOOK_URL = f'https://api.telegram.org/bot{os.environ["TELEGRAM_WEBHOOK_KEY"]}/'  # <-- add your telegram token as environment variable

        url = TELEGRAM_WEBHOOK_URL + 'sendMessage'
        response = requests.post(url, json=self.message)
        if response.ok:
            return response
        else:
            return None


class LotteryService:
    @staticmethod
    def summary():
        url = 'https://api.elpais.com/ws/LoteriaNavidadPremiados?n=resumen'
        headers = {"Content-type": "application/json"}
        response = requests.get(url, headers=headers)

        awarded_numbers = json.loads(response.text[8:])
        if response.ok:
            return awarded_numbers
        else:
            return None
