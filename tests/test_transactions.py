from conftest import get_token


def test_create_transaction(test_client):

    token = get_token(test_client)

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = test_client.post(
        "/transactions",
        headers=headers,
        json={
            "description": "Salário",
            "value": 5000,
            "type": "income",
            "date": "2026-03-01",
            "category_id": 1
        }
    )

    assert response.status_code == 200