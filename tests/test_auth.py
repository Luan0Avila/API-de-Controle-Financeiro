def test_register_user(test_client):
    response = test_client.post(
        "/auth/register",
        json={
            "email": "teste@email.com",
            "password":"123456"
        }
    )

    assert response.status_code == 200

def test_login_user(test_client):
    response = test_client.post(
        "/auth/login",
        json={
            "email": "teste@email.com",
            "password": "123456"
        }
    )

    data = response.json()

    assert response.status_code == 200
    assert "access_token" in data