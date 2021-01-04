import os
import pytest
import requests
import requests_mock

try:
    from.temp_env_var import TEMP_ENV_VARS, ENV_VARS_TO_SUSPEND
except ImportError:
    TEMP_ENV_VARS = {}
    ENV_VARS_TO_SUSPEND  = []

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
    return {'message': {'chat': {'id': 1},'text': 'hi'}}

@pytest.fixture
def telegram_url_sendMessage():
    return 'https://api.telegram.org/bot/sendMessage'

@pytest.fixture
def telegram_sendMessage(requests_mock,telegram_url_sendMessage, message):
    requests_mock.post(telegram_url_sendMessage, json=message, status_code=200)