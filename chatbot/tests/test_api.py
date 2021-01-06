from unittest import mock

import pytest
from flask import json
from chatbot.services import TelegramMessageService
from chatbot.tests.helper import MockResponse


def test_salute(client):
    response = client.get('/')
    assert response.data == b'Hello, World!'


@mock.patch('requests.post')
def test_when_start_chat_bot_list_awarded_numbers(mock_post,
                                                  client,
                                                  christmas_lottery_winners,
                                                  request_message,
                                                  response_message):
    response = MockResponse(response_message, 200)
    mock_post.return_value = response

    response = client.post(
        '/',
        data=json.dumps(request_message),
        content_type='application/json',
    )
    awarded_numbers = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert awarded_numbers == json.loads(christmas_lottery_winners)
