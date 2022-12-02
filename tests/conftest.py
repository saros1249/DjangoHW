from pytest_factoryboy import register

from tests.factories import AdsFactory, SelectionFactory

pytest_plugins = "tests.fixtures"

register(AdsFactory)
register(SelectionFactory)