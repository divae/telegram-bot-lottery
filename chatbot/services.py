import requests
from flask import json

from chatbot.constants import TELEGRAM_WEBHOOK_URL, URL_CHRISTMAS_LOTTERY_SUMMARY


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
        url = TELEGRAM_WEBHOOK_URL + 'sendMessage'
        response = requests.post(url, json=self.message)

        return response


class LotteryService:
    @staticmethod
    def summary():
        headers = {"Content-type": "application/json"}
        response = requests.get(URL_CHRISTMAS_LOTTERY_SUMMARY, headers=headers)

        awarded_numbers = json.loads(response.text[8:])

        return awarded_numbers
