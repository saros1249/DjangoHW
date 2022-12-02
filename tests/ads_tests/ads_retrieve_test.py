import pytest


@pytest.mark.django_db
def test_retrieve_ads(client, ads, hr_token):
    expected_response = {
        "id": 1,
        "name": "TestText",
        "author": "TestUsername",
        "price": 1000,
        "description": None,
        "is_published": False,
        "category": None,
    }

    response = client.get(
        f"/ad/{ads.pk}/",
        HTTP_AUTHORIZATION="Token " + hr_token
    )

    assert response.status_code == 200
    assert response.data == expected_response
