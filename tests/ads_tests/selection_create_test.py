import pytest


@pytest.mark.django_db
def test_create_selection(client, ads, hr_token):
    expected_response = {
        "id": 1,
        "name": "Test",
        "owner": 1,
        "items": [ads.pk]
    }

    response = client.post(
        "/selection/create/",
        {"name": "Test", "owner": 1, "items": [ads.pk]},
        format="json",
        HTTP_AUTHORIZATION="Token " + hr_token)
    print(response.data)

    assert response.status_code == 201
    assert response.data == expected_response
