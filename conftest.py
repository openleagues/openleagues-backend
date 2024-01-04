import pytest
from pytest_factoryboy import register
from openleagues_tests.factories import UserFactory,  LocationFactory, LeaguesEventFactory, TeamFactory
from django.test import Client

@pytest.fixture
def client():
    return Client()


register(UserFactory)
register(LocationFactory)
register(LeaguesEventFactory)

@pytest.fixture
def base_user(db, user_factory):
    new_user = user_factory.create()
    return new_user

@pytest.fixture
def super_user(db, user_factory):
    super_user = user_factory.create(is_staff=True, is_superuser=True)
    return super_user

@pytest.fixture
def base_league_event(db, leagues_event_factory):
    new_event = leagues_event_factory.create()
    return new_event

@pytest.fixture
def base_location(db, location_factory):
    new_location = location_factory.create()
    return new_location
