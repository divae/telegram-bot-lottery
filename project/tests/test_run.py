from flask import json
from project.services import TelegramWebHookService

def test_salute(client):
    response = client.get('/')
    assert response.data == b'Hello, World!'

def test_when_start_chat_bot_then_process_message(client):
     message = 'Hello'
     chat_id = 1
     message_data = {'message': {'chat': {'id': chat_id},'text': message}}

     response = client.post(
         '/',
         data=json.dumps(message_data),
         content_type='application/json',
     )
     data = json.loads(response.get_data(as_text=True))

     assert response.status_code == 200
     assert data['chat_id'] == chat_id
     assert data['text'] == message