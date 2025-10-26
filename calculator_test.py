from calculator import Calculator

def test_sum():
  calculator = Calculator(3, 5)
  assert calculator.sum() == 8

def test_subtract():
  calculator = Calculator(3, 5)
  assert calculator.subtract() == -2

def test_multiply():
  calculator = Calculator(3, 5)
  assert calculator.multiply() == 15

def test_divide():
  calculator = Calculator(3, 5)
  assert calculator.divide() == 3/5
