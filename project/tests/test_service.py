from flask import json

from project.services import TelegramWebHookService, LotteryService
from project.tests.helper import MockResponse


def test_send_message(telegram_sendMessage, message):
    response = TelegramWebHookService().send_message(message)

    assert response.status_code == 200


def test_process(message):
    response = MockResponse(message, 200)

    message = TelegramWebHookService().process(response)

    assert message['chat_id'] == 1
    assert message['text'] == 'hi'


def test_summary_is_the_winning_numbers_when_the_draw_is_over(christmas_lottery_winners,
                                                              mock_request_lottery_winners):
    awarded_numbers = LotteryService.summary()

    assert awarded_numbers == json.loads(christmas_lottery_winners)
