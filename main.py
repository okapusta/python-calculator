# save this as app.py
from flask import Flask, jsonify, request
from calculator import Calculator

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/calculate")
def calculate():
    op   = request.args.get('op', type=str)
    arg1 = request.args.get('arg1', type=int)
    arg2 = request.args.get('arg2', type=int)

    calculator = Calculator(arg1, arg2)

    if not op:
      return jsonify({ "error": "missing operation" })
    if not arg1 or not arg2:

      return jsonify({ "error": "missing numbers" })

    if op == 'sum':
        return jsonify({ "result": calculator.sum() })
    if op == 'subtract':
        return jsonify({ "result": calculator.subtract() })
    if op == 'multiply':
        return jsonify({ "result": calculator.multiply() })
    if op == 'divide':
        return jsonify({ "result": calculator.divide() })

if __name__ == '__main__':
    app.run(debug=True)
