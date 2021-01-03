import pytest

from app import create_chatbot


@pytest.fixture
def app():
    app = create_chatbot()
    return app
