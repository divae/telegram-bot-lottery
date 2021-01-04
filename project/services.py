import os
import requests

class TelegramWebHookService:
    def send_message(self, json_data):
        TELEGRAM_WEBHOOK_URL = f'https://api.telegram.org/bot{os.environ["TELEGRAM_WEBHOOK_CODE"]}/'  # <-- add your telegram token as environment variable

        url = TELEGRAM_WEBHOOK_URL + 'sendMessage'
        response = requests.post(url, json=json_data)
        if response.ok:
            return response
        else:
            return None

    def process(self, request):
        request_message = request.get_json()
        chat_id = request_message['message']['chat']['id']
        message = request_message['message']['text']

        self.message = {
           "chat_id": chat_id,
           "text": message,
        }

        return self.message

