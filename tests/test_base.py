
def test_salute(client):
    response = client.get('/')
    assert response.data == b'Hello, World!'
