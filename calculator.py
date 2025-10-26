""""
This is a calculator module
"""

class Calculator:
    """
    Calculator class
    """
    def __init__(self, op1: float, op2: float):
        self.op1 = op1
        self.op2 = op2

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
        return self.op1 / self.op2
