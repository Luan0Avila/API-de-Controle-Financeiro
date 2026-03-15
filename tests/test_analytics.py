def test_income_vs_expense(test_client):

    token = get_token(test_client)

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = test_client.get(
        "/analytics/income-vs-expense",
        headers=headers
    )

    assert response.status_code == 200