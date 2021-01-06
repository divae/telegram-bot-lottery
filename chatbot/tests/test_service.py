from unittest import mock

import pytest
import requests
from flask import json

from chatbot.services import LotteryService
from chatbot.tests.helper import MockResponse


def test_telegram_change_message(telegram_message_service, response_message):
    text = 'new'
    new = {'chat_id': 1, 'text': text}
    assert telegram_message_service.message == response_message

    telegram_message_service.change_message(text)

    assert telegram_message_service.message == new


def test_telegram_message_process(telegram_message_service):
    chat_id = 1
    text = 'hi'

    message = telegram_message_service.process()

    assert message['chat_id'] == chat_id
    assert message['text'] == text


def test_telegram_message(telegram_message_service):
    chat_id = 1
    text = 'hi'

    message = telegram_message_service.message

    assert message['chat_id'] == chat_id
    assert message['text'] == text


@mock.patch('requests.post')
def test_telegram_message_send(mock_post, telegram_message_service, response_message):
    response = MockResponse(response_message, 200)
    mock_post.return_value = response

    response = telegram_message_service.send()
    text = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert text == response_message


@mock.patch('requests.post')
def test_summary_is_the_winning_numbers_when_the_draw_is_over(mock_post, christmas_lottery_winners):
    response = MockResponse(christmas_lottery_winners, 200)
    mock_post.return_value = response

    awarded_numbers = LotteryService.summary()

    assert awarded_numbers == json.loads(christmas_lottery_winners)
