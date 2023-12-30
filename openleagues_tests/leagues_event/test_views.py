import pytest
from openleagues.leagues_event.models import LeaguesEvent
from openleagues.leagues_event.serializers import LeaguesEventSerializer

@pytest.mark.django_db
def test_leagues_event_list_get(client, base_league_event):
    # Send a GET request to the view
    response = client.get('/api/v1/leagues/')

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200

    # Check that the returned data matches the serialized data of all LeaguesEvent instances
    expected_data = LeaguesEventSerializer(LeaguesEvent.objects.all(), many=True).data
    assert response.json() == expected_data
