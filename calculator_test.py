from calculator import Calculator
import pytest

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


@pytest.mark.parametrize("a, b, expected", [
      (2, 3, 5),
      (-1, -2, -3),
      (2.5, 3.5, 6.0),
  ])
def test_add_parametrized(a, b, expected):
    calc = Calculator(a, b)
    assert calc.sum() == expected
