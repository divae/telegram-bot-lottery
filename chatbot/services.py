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
            - %s
            - %s
            
        Premio a las 3 cifras:
            - %s
            - %s
            - %s
            - %s
            - %s
            - %s
            - %s
            - %s
            - %s
            - %s
            - %s
            - %s
            - %s
            - %s
            
        Premio a las 2 cifras:
            - %s
            - %s
            - %s
            - %s
            - %s
            
        Reintegros:
            - %s
            - %s
            - %s
            
        ¡SUERTE!
        """ % (self.text['fraseTexto'],
               sin_datos if self.text['premio1'] == -1 else self.text['premio1'],
               sin_datos if self.text['premio2'] == -1 else self.text['premio2'],
               sin_datos if self.text['premio3'] == -1 else self.text['premio3'],
               sin_datos if self.text['extracciones4cifras'][0] == -1 else self.text['extracciones4cifras'][0],
               sin_datos if self.text['extracciones4cifras'][1] == -1 else self.text['extracciones4cifras'][1],
               sin_datos if self.text['extracciones4cifras'][2] == -1 else self.text['extracciones4cifras'][2],
               sin_datos if self.text['extracciones4cifras'][3] == -1 else self.text['extracciones4cifras'][3],
               sin_datos if self.text['extracciones4cifras'][4] == -1 else self.text['extracciones4cifras'][4],
               sin_datos if self.text['extracciones4cifras'][5] == -1 else self.text['extracciones4cifras'][5],
               sin_datos if self.text['extracciones4cifras'][6] == -1 else self.text['extracciones4cifras'][6],
               sin_datos if self.text['extracciones4cifras'][7] == -1 else self.text['extracciones4cifras'][7],
               sin_datos if self.text['extracciones4cifras'][8] == -1 else self.text['extracciones4cifras'][8],
               sin_datos if self.text['extracciones4cifras'][9] == -1 else self.text['extracciones4cifras'][9],
               sin_datos if self.text['extracciones4cifras'][10] == -1 else self.text['extracciones4cifras'][10],
               sin_datos if self.text['extracciones4cifras'][11] == -1 else self.text['extracciones4cifras'][11],
               sin_datos if self.text['extracciones4cifras'][12] == -1 else self.text['extracciones4cifras'][12],
               sin_datos if self.text['extracciones4cifras'][13] == -1 else self.text['extracciones4cifras'][13],
               sin_datos if self.text['extracciones2cifras'][0] == -1 else self.text['extracciones2cifras'][0],
               sin_datos if self.text['extracciones2cifras'][1] == -1 else self.text['extracciones2cifras'][1],
               sin_datos if self.text['extracciones2cifras'][2] == -1 else self.text['extracciones2cifras'][2],
               sin_datos if self.text['extracciones2cifras'][3] == -1 else self.text['extracciones2cifras'][3],
               sin_datos if self.text['extracciones2cifras'][4] == -1 else self.text['extracciones2cifras'][4],
               sin_datos if self.text['reintegros'][0] == -1 else self.text['reintegros'][0],
               sin_datos if self.text['reintegros'][1] == -1 else self.text['reintegros'][1],
               sin_datos if self.text['reintegros'][2] == -1 else self.text['reintegros'][2]
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
