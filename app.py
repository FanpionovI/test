from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    if 'num1' not in data or 'num2' not in data:
        return jsonify({'error': 'Missing num1 or num2'}), 400
    try:
        result = float(data['num1']) + float(data['num2'])
        return jsonify({'result': result}), 200
    except ValueError:
        return jsonify({'error': 'Invalid numbers'}), 400

@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    if 'num1' not in data or 'num2' not in data:
        return jsonify({'error': 'Missing num1 or num2'}), 400
    try:
        result = float(data['num1']) - float(data['num2'])
        return jsonify({'result': result}), 200
    except ValueError:
        return jsonify({'error': 'Invalid numbers'}), 400

@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    if 'num1' not in data or 'num2' not in data:
        return jsonify({'error': 'Missing num1 or num2'}), 400
    try:
        result = float(data['num1']) * float(data['num2'])
        return jsonify({'result': result}), 200
    except ValueError:
        return jsonify({'error': 'Invalid numbers'}), 400

@app.route('/divide', methods=['POST'])
def divide():
    data = request.get_json()
    if 'num1' not in data or 'num2' not in data:
        return jsonify({'error': 'Missing num1 or num2'}), 400
    try:
        num2 = float(data['num2'])
        if num2 == 0:
            return jsonify({'error': 'Division by zero'}), 400
        result = float(data['num1']) / num2
        return jsonify({'result': result}), 200
    except ValueError:
        return jsonify({'error': 'Invalid numbers'}), 400

@app.route('/')
def home():
    return "Flask Calculator API"

if __name__ == '__main__':
    app.run(debug=True)