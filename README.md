[![Python application](https://github.com/okapusta/python-calculator/actions/workflows/python-app.yml/badge.svg)](https://github.com/okapusta/python-calculator/actions/workflows/python-app.yml)


Simple calculator
-----


Running:
```
uv run python main.py
```

Testing:

```
uv run pytest
```

Calculator Example:

```python
calculator = Calculator(3, 5)
calculator.sum()
```

API Example:
```
curl http://127.0.0.1:5000/calculate\?op\=multiply\&arg1\=2\&arg2\=5


{
  "result": 10
}
```
