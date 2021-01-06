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
            "text": self.format_HTML(),
        }

    def format_HTML(self):
        sin_datos = 'Sin datos'
        return """%s
        
        1º Premio: %s
        2º Premio: %s
        3º Premio: %s
        
        Premio a las 4 cifras:
            %s
            %s
            
        Premio a las 3 cifras:
            %s
            %s
            %s
            %s
            %s
            %s
            %s
            %s
            %s
            %s
            %s
            %s
            %s
            %s
            
        Premio a las 2 cifras:
            %s
            %s
            %s
            %s
            %s
            
        Reintegros:
            %s
            %s
            %s
            
        ¡SUERTE!
        """ % (self.text['fraseTexto'],
               sin_datos if self.text['premio1'] == -1 else self.text['premio1'],
               sin_datos if self.text['premio2'] == -1 else self.text['premio2'],
               sin_datos if self.text['premio3'] == -1 else self.text['premio3'],
               self.text['extracciones4cifras'][0],
               self.text['extracciones4cifras'][1],
               self.text['extracciones3cifras'][0],
               self.text['extracciones3cifras'][1],
               self.text['extracciones3cifras'][2],
               self.text['extracciones3cifras'][3],
               self.text['extracciones3cifras'][4],
               self.text['extracciones3cifras'][5],
               self.text['extracciones3cifras'][6],
               self.text['extracciones3cifras'][7],
               self.text['extracciones3cifras'][8],
               self.text['extracciones3cifras'][9],
               self.text['extracciones3cifras'][10],
               self.text['extracciones3cifras'][11],
               self.text['extracciones3cifras'][12],
               self.text['extracciones3cifras'][13],
               self.text['extracciones2cifras'][0],
               self.text['extracciones2cifras'][1],
               self.text['extracciones2cifras'][2],
               self.text['extracciones2cifras'][3],
               self.text['extracciones2cifras'][4],
               self.text['reintegros'][0],
               self.text['reintegros'][1],
               self.text['reintegros'][2]
               )

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
