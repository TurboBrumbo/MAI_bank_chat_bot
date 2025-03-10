from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.json.get('message')

    rasa_url = "http://localhost:5005/webhooks/rest/webhook"
    payload = {
        "sender": "user",
        "message": user_message
    }

    response = requests.post(rasa_url, json=payload)

    if response.status_code == 200:
        rasa_response = response.json()
        if rasa_response:
            bot_response = rasa_response[0]['text']
        else:
            bot_response = "Извините, я не могу ответить."
    else:
        bot_response = "Ошибка при обращении к Rasa."

    return jsonify({'response': bot_response})


if __name__ == '__main__':
    app.run(debug=True)