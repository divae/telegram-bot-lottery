import requests
from flask import json
from project.services import TelegramWebHookService


def test_salute(client):
    response = client.get('/')
    assert response.data == b'Hello, World!'


def test_when_start_chat_bot_list_awarded_numbers(client,
                                                  mock_request_lottery_winners,
                                                  christmas_lottery_winners,
                                                  message,
                                                  mocker):
    hook_send_message = mocker.patch.object(TelegramWebHookService, 'send_message')

    response = client.post(
        '/',
        data=json.dumps(message),
        content_type='application/json',
    )
    awarded_numbers = json.loads(response.get_data(as_text=True))

    hook_send_message.assert_called_with(awarded_numbers)
    assert response.status_code == 200
    assert awarded_numbers == json.loads(christmas_lottery_winners)
