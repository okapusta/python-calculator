from numbers import Number

""""
This is the calculator module
"""

class InvalidArgumentException(ValueError):
    """
    Raised when either of arguments is invalid
    """

    pass
class Calculator:
    """
    Calculator class
    """
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

