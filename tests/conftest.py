import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

@pytest.fixture
def test_client():
    return client


def get_token(client):

    client.post(
        "/auth/register",
        json={
                "email": "user@text.com",
                "password": "123456"
        }
    )

    response = client.post(
        "/auth/login",
        json={
            "email": "user@test.com",
            "password": "123456"
        }
    )
    
    return response.json()["access_token"]