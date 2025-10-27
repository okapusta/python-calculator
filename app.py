""""
This is a calculator webservice
"""

from flask import Flask, jsonify, request
from calculator import Calculator

def create_app():
    app = Flask(__name__)

    @app.route("/", methods=["GET"])
    def hello():
        """"
        Healthcheck
        """

        return "Hello, World!"

    @app.route("/calculate", methods=["POST"])
    def calculate():
        """"
        Calculator API
        """
        print(request.args)
        op   = request.args.get('op', type=str)
        arg1 = request.args.get('arg1', type=int)
        arg2 = request.args.get('arg2', type=int)

        if not op:
            return jsonify({ "error": "missing operation" }), 400
        if not arg1 or not arg2:
            return jsonify({ "error": "missing numbers" }), 400

        result = __run_calculations(op, arg1, arg2)

        return jsonify({ "result": result })

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

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
