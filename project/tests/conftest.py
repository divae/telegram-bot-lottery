import os
import pytest
import requests
import requests_mock

from run import create_chatbot

def pytest_generate_tests(metafunc):
    os.environ['TELEGRAM_WEBHOOK_URL'] = '1111'

@pytest.fixture
def app():
    app = create_chatbot()
    return app

@pytest.fixture
def os_telegram_webhook():
    code = '1111'
    os.environ['TELEGRAM_WEBHOOK_URL'] = code
    return code

@pytest.fixture
def message():
    return {'message': {'chat': {'id': 1},'text': 'hi'}}

@pytest.fixture
def telegram_url_sendMessage():
    return 'https://api.telegram.org/bot/sendMessage'

@pytest.fixture
def telegram_sendMessage(requests_mock,telegram_url_sendMessage, message):
    requests_mock.post(telegram_url_sendMessage, json=message, status_code=200)

