from flask import Flask, request, jsonify, render_template
from basicmodel import generate_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('template.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    response = generate_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
