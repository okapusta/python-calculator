""""
This is a calculator webservice
"""

from flask import Flask, jsonify, request
from calculator import Calculator, InvalidOperationException
from schemas import CalculationSchema
from marshmallow import ValidationError

def create_app():
    """"
    Creates flask app
    """

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

        try:
            parsed = CalculationSchema().load(request.args)
            result = Calculator.calculate(parsed['op'], parsed['arg1'], parsed['arg2'])
            return jsonify({ "result": result })
        except ValidationError as err:
            return jsonify({ "error": err.messages }), 400

    return app

if __name__ == '__main__':
    calculator_app = create_app()
    calculator_app.run(debug=True)
