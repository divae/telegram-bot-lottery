import os
import pytest
import requests

from chatbot.tests.helper import MockResponse
from chatbot.services import TelegramMessageService

try:
    from chatbot.tests.config.temp_env_var import TEMP_ENV_VARS, ENV_VARS_TO_SUSPEND
except ImportError:
    TEMP_ENV_VARS = {}
    ENV_VARS_TO_SUSPEND = []


@pytest.fixture(scope="session", autouse=True)
def tests_setup_and_teardown():
    """
    Article https://medium.com/@shay.palachy/temp-environment-variables-for-pytest-7253230bd777
    """
    # Will be executed before the first test
    old_environ = dict(os.environ)
    os.environ.update(TEMP_ENV_VARS)
    for env_var in ENV_VARS_TO_SUSPEND:
        os.environ.pop(env_var, default=None)

    yield
    # Will be executed after the last test
    os.environ.clear()
    os.environ.update(old_environ)


@pytest.fixture
def app():
    from run import create_chatbot

    app = create_chatbot()
    return app


@pytest.fixture
def request_message():
    return {'message': {'chat': {'id': 1}, 'text': 'hi'}}


@pytest.fixture
def telegram_message_service(request_message):
    request = MockResponse(request_message, 200)
    return TelegramMessageService(request)


@pytest.fixture
def telegram_url_send_message():
    return 'https://api.telegram.org/bot/sendMessage'


@pytest.fixture
def response_message():
    return {'chat_id': 1, 'text': 'hi'}


@pytest.fixture
def mock_request_message_send(response_message, mocker):
    response = MockResponse(response_message, 200)
    mocker.patch.object(requests, 'post', response)

@pytest.fixture
def christmas_lottery_winners():
    return '{"timestamp":1608655774,"status":4,"numero1":72897,"numero2":6095,"numero3":52472,"numero4":75981,"numero5":38341,"numero6":86986,"numero7":37023,"numero8":19371,"numero9":49760,"numero10":55483,"numero11":28674,"numero12":43831,"numero13":31617,"fraseSorteoPDF":"Buscador y PDF con la lista oficial","fraseListaPDF":"Buscador y PDF con la lista oficial","listaPDF":"http://servicios.elpais.com/sorteos/loteria-navidad/lista-oficial-loteria-navidad/","urlAudio":"","error":0}'


@pytest.fixture
def mock_request_lottery_winners(christmas_lottery_winners, mocker):
    response = MockResponse(christmas_lottery_winners, 200)
    mocker.patch.object(requests, 'post', response)

