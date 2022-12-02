import factory.django
from ads.models import Ads, Selection


class AdsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ads

    name = "TestText"
    author = "TestUsername"
    price = 1000


class SelectionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Selection

    name = "test"

