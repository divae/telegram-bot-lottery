import os

from bot.api import create_chatbot

app = create_chatbot()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
