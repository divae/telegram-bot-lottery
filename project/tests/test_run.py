import requests
from flask import json
from project.services import TelegramMessageService


def test_salute(client):
    response = client.get('/')
    assert response.data == b'Hello, World!'


def test_when_start_chat_bot_list_awarded_numbers(client,
                                                  mock_request_lottery_winners,
                                                  christmas_lottery_winners,
                                                  request_message,
                                                  mocker):
    mocker.patch.object(TelegramMessageService, 'send')

    response = client.post(
        '/',
        data=json.dumps(request_message),
        content_type='application/json',
    )
    awarded_numbers = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert awarded_numbers == json.loads(christmas_lottery_winners)
