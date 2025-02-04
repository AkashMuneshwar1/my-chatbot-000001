from flask import Flask, render_template, request, jsonify
from chatbot_logic import get_response_and_next_questions

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    current_question = request.json.get('current_question')
    response, next_questions = get_response_and_next_questions(current_question)
    return jsonify({"response": response, "next_questions": next_questions})

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=5000)
