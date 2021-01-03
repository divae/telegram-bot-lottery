import pytest


from project.services import TelegramWebHookService

class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def get_json(self):
        return self.json_data

def test_send_message(telegram_sendMessage, message):
    response = TelegramWebHookService().send_message(message)

    assert response.status_code == 200

def test_process(message):
     response = MockResponse(message, 200)

     message = TelegramWebHookService().process(response)

     assert message['chat_id'] == 1
     assert message['text'] == 'hi'