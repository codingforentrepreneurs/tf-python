import os
from fastapi.testclient import TestClient
import pytest

# Assuming your FastAPI code is in a file named `main.py`
from .main import app, get_env_message, get_secret_message

client = TestClient(app)

def test_home_view():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "hello": "world",
        "cron": "smooth-cronjob",
        "watchtower": "working",
        "env-message": get_env_message(),
        "secret-message": get_secret_message(),
    }

@pytest.fixture(autouse=True)
def clear_env_message(monkeypatch):
    monkeypatch.delenv("ENV_MESSAGE", raising=False)

    
def test_env_message_set(monkeypatch):
    monkeypatch.setenv("ENV_MESSAGE", "Test message")
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["env-message"] == "Test message"


@pytest.fixture(autouse=True)
def clear_secret_message(monkeypatch):
    monkeypatch.delenv("SECRET_MESSAGE", raising=False)

    
def test_secret_message_set(monkeypatch):
    monkeypatch.setenv("SECRET_MESSAGE", "Test secret message")
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["secret-message"] == "Test secret message"
