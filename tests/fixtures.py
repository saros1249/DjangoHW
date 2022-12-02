import pytest


@pytest.fixture
@pytest.mark.django_db
def hr_token(client, django_user_model):
    password = "123qwe"
    username = "TestUsername"
    birth_date = "2000-12-08"
    email = "sd@mail.ru"
    location = "London"

    django_user_model.objects.create_user(
        username=username, password=password, birth_date=birth_date, email=email
    )

    response = client.post(
        "/user/login/",
        {"username": username, "password": password},
        format="json"
    )

    return response.data["token"]