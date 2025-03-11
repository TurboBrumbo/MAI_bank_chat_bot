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

    print("Rasa response status code:", response.status_code)
    print("Rasa response JSON:", response.json())

    if response.status_code == 200:
        rasa_response = response.json()
        if rasa_response:
            bot_responses = [msg['text'] for msg in rasa_response if 'text' in msg]
        else:
            bot_responses = ["Извините, я не могу ответить."]
    else:
        bot_responses = ["Ошибка при обращении к Rasa."]

    print("Bot responses:", bot_responses)

    return jsonify({'responses': bot_responses})


if __name__ == '__main__':
    app.run(debug=True)