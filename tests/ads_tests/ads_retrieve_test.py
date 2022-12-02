import pytest


@pytest.mark.django_db
def test_retrieve_ads(client, ads, hr_token):
    expected_response = {
        "id": ads.pk,
        "name": "TestText",
        "author": None,
        "price": 1000,
        "description": None,
        "is_published": False,
        "image": None,
        "category": None,
    }

    response = client.get(
        f"/ad/{ads.pk}/",
        HTTP_AUTHORIZATION="Token " + hr_token
    )

    assert response.status_code == 200
    assert response.data == expected_response
