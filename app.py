from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# A simple set of responses
responses = {
    "hi": "Hello! How can I help you?",
    "how are you?": "I'm just a bot, but thanks for asking!",
    "bye": "Goodbye! Have a great day!",
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message').lower()
    response_message = responses.get(user_message, "I'm sorry, I don't understand that.")
    return jsonify({"response": response_message})

if __name__ == '__main__':
    app.run(debug=True)
