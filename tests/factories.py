import factory.django
from ads.models import Ads, Selection
from users.models import User


class AdsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ads

    name = "TestText"
    price = 1000


class SelectionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Selection

    name = "test"

