""""
This is the calculator module
"""

from numbers import Number

class InvalidArgumentException(ValueError):
    """
    Raised when either of arguments is invalid
    """
class InvalidOperationException(ValueError):
    """
    Raised when operations is invalid
    """
class Calculator:
    """
    Calculator class
    """
    @classmethod
    def calculate(cls, operation, arg1, arg2):
        """
        Constructs calculator and runs appropriate operation

        Raises InvalidOperationException
        """
        calculator = cls(arg1, arg2)
        if operation == 'sum':
            return calculator.sum()
        if operation == 'subtract':
            return calculator.subtract()
        if operation == 'multiply':
            return calculator.multiply()
        if operation == 'divide':
            return calculator.divide()

        raise InvalidOperationException(f"Invalid operation {operation}")

    def __init__(self, op1: float, op2: float):
        self.op1 = op1
        self.op2 = op2

        self.__validate_arguments()

    def sum(self):
        """
        Sums two numbers
        """
        return self.op1 + self.op2

    def subtract(self):
        """
        Subtracts two numbers
        """
        return self.op1 - self.op2

    def multiply(self):
        """
        Multiplies two numbers
        """
        return self.op1 * self.op2

    def divide(self):
        """
        Divides two numbers
        """
        if self.op2 == 0:
            return 0
        return self.op1 / self.op2

    def __validate_arguments(self):
        if not isinstance(self.op1, Number) or not isinstance(self.op2, Number):
            raise InvalidArgumentException("invalid arguments")
