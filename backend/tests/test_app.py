import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_login_success(client):
    rv = client.post('/login', json=dict(username='admin', password='admin'))
    assert rv.status_code == 200
    assert b"Welcome to DevOps Bot" in rv.data

def test_login_failure(client):
    rv = client.post('/login', json=dict(username='admin', password='wrong'))
    assert rv.status_code == 401
    assert b"Invalid Credentials" in rv.data
