import pytest
from ads.serializers import AdsListSerializer

from tests.factories import AdsFactory


@pytest.mark.django_db
def test_list_ads(client):
    ads = AdsFactory.create_batch(10)
    expected_response = {
        "count": 10,
        "next": None,
        "previous": None,
        "results": AdsListSerializer(ads, many=True).data}

    response = client.get("/ad/")

    assert response.status_code == 200
    assert response.data == expected_response
