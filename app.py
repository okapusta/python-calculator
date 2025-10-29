""""
This is a calculator webservice
"""

from flask import Flask, jsonify, request
from calculator import Calculator, InvalidOperationException

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

        op   = request.args.get('op', type=str)
        arg1 = request.args.get('arg1', type=int)
        arg2 = request.args.get('arg2', type=int)

        if not op:
            return jsonify({ "error": "missing operation" }), 400
        if not arg1 or not arg2:
            return jsonify({ "error": "missing numbers" }), 400

        try:
            result = Calculator.calculate(op, arg1, arg2)

            return jsonify({ "result": result })
        except InvalidOperationException:
            return jsonify({ "error": "invalid operation" }), 400

    return app

if __name__ == '__main__':
    test_app = create_app()
    test_app.run(debug=True)
