from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Web Calculator API! Use /add, /subtract, /multiply, or /divide with GET parameters 'a' and 'b'."

@app.route('/add')
def add():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    return jsonify(result=a + b)

@app.route('/subtract')
def subtract():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    return jsonify(result=a - b)

@app.route('/multiply')
def multiply():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    return jsonify(result=a * b)

@app.route('/divide')
def divide():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 1))  # avoid division by zero
    if b == 0:
        return jsonify(error="Division by zero is not allowed"), 400
    return jsonify(result=a / b)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
