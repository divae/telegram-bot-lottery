import os
import requests
from flask import json


class TelegramWebHookService:
    def process(self, request):
        request_message = request.get_json()
        chat_id = request_message['message']['chat']['id']
        message = request_message['message']['text']

        message_processed = {
            "chat_id": chat_id,
            "text": message,
        }

        return message_processed

    def send_message(self, json_data):
        TELEGRAM_WEBHOOK_URL = f'https://api.telegram.org/bot{os.environ["TELEGRAM_WEBHOOK_KEY"]}/'  # <-- add your telegram token as environment variable

        url = TELEGRAM_WEBHOOK_URL + 'sendMessage'
        response = requests.post(url, json=json_data)
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
