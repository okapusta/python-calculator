from calculator import Calculator, InvalidArgumentException
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

def test_division_by_zero():
  calculator = Calculator(3, 0)
  assert calculator.divide() == 0

def test_any_argument_string():
  with pytest.raises(InvalidArgumentException) as error:
    Calculator(3, "tester")
  assert str(error.value) == "invalid arguments"


@pytest.mark.parametrize("a, b, expected", [
      (2, 3, 5),
      (-1, -2, -3),
      (2.5, 3.5, 6.0),
  ])
def test_add_parametrized(a, b, expected):
    calc = Calculator(a, b)
    assert calc.sum() == expected

@pytest.mark.parametrize("m, a, b, expected", [
      ('sum', 2, 3, 5),
      ('subtract', -1, -2, 1),
      ('multiply', 4, 4, 16.0),
      ('divide', 6, 2, 3.0),
  ])
def test_class_calculate(m, a, b, expected):
    result = getattr(Calculator, 'calculate')(m, a, b)
    assert result == expected
