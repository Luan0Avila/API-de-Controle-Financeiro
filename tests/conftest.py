import pytest
from fastapi.testclient import TestClient

from app.main import app

@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def user_token(client):
    email = "user@test.com"
    password = "123456"

    client.post(
        "/auth/register",
        json={
            "email": email,
            "password": password
        }
    )

    response = client.post(
        "/auth/login",
        json={
            "email": email,
            "password": password
        }
    )

    return response.json()["access_token"]