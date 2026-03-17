import uuid

def test_register_user(client):
    email = f"test_{uuid.uuid4()}@email.com"

    response = client.post("/auth/register", json={
        "email": email,
        "password": "123456"
    })

    print(response.text)

    assert response.status_code == 200

def test_login_user(test_client):
    response = test_client.post(
        "/auth/login",
        json={
            "email": "teste2@email.com",
            "password": "123456"
        }
    )

    data = response.json()

    assert response.status_code == 200
    assert "access_token" in data