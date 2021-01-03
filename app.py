from flask import Flask


def create_chatbot():
    app = Flask(__name__)

    @app.route('/')
    def salute():
        return 'Hello, World!'

    return app


app = create_chatbot()
