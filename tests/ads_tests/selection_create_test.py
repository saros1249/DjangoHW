import pytest


@pytest.mark.django_db
def test_create_selection(client, hr_token):
    expected_response = {
        "id": 1,
        "owner": 1
    }

    data = {
        "owner": "1",
    }


    response = client.post(
        "/selection/create/",
        data,
        format="json",
        HTTP_AUTHORIZATION="Token " + hr_token
    )

    assert response.status_code == 201
    assert response.data == expected_response
