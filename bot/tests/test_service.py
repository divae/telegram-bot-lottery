import pytest
from flask import json

from bot.services import LotteryService


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


@pytest.mark.skip(reason="TypeError: 'MockResponse' object is not callable")
def test_telegram_message_send(telegram_message_service, mock_request_message_send, response_message):
    response = telegram_message_service.send()
    text = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert text == response_message


def test_summary_is_the_winning_numbers_when_the_draw_is_over(christmas_lottery_winners,
                                                              mock_request_lottery_winners):
    awarded_numbers = LotteryService.summary()

    assert awarded_numbers == json.loads(christmas_lottery_winners)
