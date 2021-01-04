from flask import json
from project.services import TelegramWebHookService
from pytest_mock import mocker

def test_salute(client):
    response = client.get('/')
    assert response.data == b'Hello, World!'

def test_when_start_chat_bot_then_process_message_and_return_it(client, mocker):
     message = 'Hello'
     chat_id = 1
     message_proccesed =  {
              "chat_id": chat_id,
              "text": message,
           }
     message_data = {'message': {'chat': {'id': chat_id},'text': message}}
     hook_send_message = mocker.patch.object(TelegramWebHookService, 'send_message')

     response = client.post(
         '/',
         data=json.dumps(message_data),
         content_type='application/json',
     )
     data = json.loads(response.get_data(as_text=True))

     hook_send_message.assert_called_with(message_proccesed)
     assert response.status_code == 200
     assert data['chat_id'] == chat_id
     assert data['text'] == message