import os

TELEGRAM_WEBHOOK_URL = f'https://api.telegram.org/bot{os.environ["TELEGRAM_WEBHOOK_KEY"]}/'  # <-- add your telegram token as environment variable
URL_CHRISTMAS_LOTTERY = 'https://api.elpais.com/ws/LoteriaNinoPremiados'
URL_CHRISTMAS_LOTTERY_SUMMARY = f'{URL_CHRISTMAS_LOTTERY}?n=resumen'