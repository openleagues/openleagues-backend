import pytest
from django.test import Client
from openleagues.leagues_event.models import LeaguesEvent
from openleagues.leagues_event.serializer import LeaguesEventSerializer

@pytest.fixture
def client():
    return Client()

# @pytest.fixture
# def base_league_event(leagues_event_factory):
#     new_event = leagues_event_factory.create()
#     return new_event

@pytest.mark.django_db
def test_leagues_event_list_get(client, base_league_event):
    # Send a GET request to the view
    response = client.get('/api/v1/leagues/')

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200

    # Check that the returned data matches the serialized data of all LeaguesEvent instances
    expected_data = LeaguesEventSerializer(LeaguesEvent.objects.all(), many=True).data
    assert response.json() == expected_data
