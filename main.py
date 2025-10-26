""""
This is a calculator webservice
"""

from flask import Flask, jsonify, request
from calculator import Calculator

app = Flask(__name__)

@app.route("/")
def hello():
    """"
    Healthcheck
    """

    return "Hello, World!"

@app.route("/calculate")
def calculate():
    """"
    Calculator API
    """

    op   = request.args.get('op', type=str)
    arg1 = request.args.get('arg1', type=int)
    arg2 = request.args.get('arg2', type=int)

    if not op:
        return jsonify({ "error": "missing operation" })
    if not arg1 or not arg2:
        return jsonify({ "error": "missing numbers" })

    return jsonify({ "result": __run_calculations(op, arg1, arg2 )})

def __run_calculations(operation, arg1, arg2):
    calculator = Calculator(arg1, arg2)

    if operation == 'sum':
        return calculator.sum()
    if operation == 'subtract':
        return calculator.subtract()
    if operation == 'multiply':
        return calculator.multiply()
    if operation == 'divide':
        return calculator.divide()

    return None

if __name__ == '__main__':
    app.run(debug=True)
