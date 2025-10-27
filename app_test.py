import pytest
import json

from app import create_app

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_valid_request(client):
    import json


def test_add_user(client):
    response = client.post(
        "/calculate", query_string={ "op": "sum", "arg1": 1, "arg2": 2 }
    )
    assert response.status_code == 200
    response_json = json.loads(response.data)
    assert response_json == { "result": 3 }


def test_missing_operation(client):
    response = client.post(
        "/calculate", query_string={ "arg1": 1, "arg2": 2 }
    )
    assert response.status_code == 400
    response_json = json.loads(response.data)
    assert response_json == { 'error': 'missing operation' }

def test_invalid_operation(client):
    response = client.post(
        "/calculate", query_string={ "op": "invalid", "arg1": 1, "arg2": 2 }
    )
    assert response.status_code == 200
    response_json = json.loads(response.data)
    assert response_json == { 'result': None }

def test_invalid_arguments(client):
    response = client.post(
        "/calculate", query_string={ "op": "sum", "arg1": "invalid", "arg2": 2 }
    )
    assert response.status_code == 400
    response_json = json.loads(response.data)
    assert response_json == { 'error': 'missing numbers' }


def test_division_by_zero_request(client):
    response = client.post(
        "/calculate", query_string={ "op": "divide", "arg1": 1, "arg2": 0 }
    )
    assert response.status_code == 400
    response_json = json.loads(response.data)
    assert response_json == { 'error': 'missing numbers' }
