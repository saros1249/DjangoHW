import pytest


@pytest.mark.django_db
def test_create_ads(client, hr_token):
    expected_response = {
        "id": 1,
        "name": "TestText",
        "author": None,
        "price": 1000,
        "description": None,
        "is_published": False,
        "category": None
    }

    data = {
        "name": "TestText",
        "price": 1000
    }

    response = client.post(
        "/ad/create/",
        data, _mutable=True,
        format="json",
        HTTP_AUTHORIZATION="Token " + hr_token
    )

    assert response.status_code == 201
    assert response.data == expected_response
