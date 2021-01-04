import os
import pytest
import requests
import requests_mock
from pytest_mock import mocker


from .helper import MockResponse

try:
    from .temp_env_var import TEMP_ENV_VARS, ENV_VARS_TO_SUSPEND
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
def message():
    return {'message': {'chat': {'id': 1}, 'text': 'hi'}}


@pytest.fixture
def telegram_url_sendMessage():
    return 'https://api.telegram.org/bot/sendMessage'


@pytest.fixture
def telegram_sendMessage(requests_mock, telegram_url_sendMessage, message):
    requests_mock.post(telegram_url_sendMessage, json=message, status_code=200)


@pytest.fixture
def christmas_lottery_winners():
    return '{"timestamp":1608655774,"status":4,"numero1":72897,"numero2":6095,"numero3":52472,"numero4":75981,"numero5":38341,"numero6":86986,"numero7":37023,"numero8":19371,"numero9":49760,"numero10":55483,"numero11":28674,"numero12":43831,"numero13":31617,"fraseSorteoPDF":"Buscador y PDF con la lista oficial","fraseListaPDF":"Buscador y PDF con la lista oficial","listaPDF":"http://servicios.elpais.com/sorteos/loteria-navidad/lista-oficial-loteria-navidad/","urlAudio":"","error":0}'

@pytest.fixture
def mock_request_lottery_winners(christmas_lottery_winners, mocker):
    response = MockResponse(christmas_lottery_winners, 200)
    mocker.patch.object(requests, 'post', response)