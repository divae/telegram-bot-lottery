import json


class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def get_json(self):
        return self.json_data

    def get_data(self, as_text):
        return json.dumps(self.json_data)
