import pytest
from factories import LeaguesEventFactory

@pytest.mark.django_db
def test_league_event_str():
    league_event = LeaguesEventFactory()
    assert league_event.__str__() == f"{league_event.title}"

def test_location_str(base_location):
    assert base_location.__str__() == f"{base_location.city}, {base_location.state} ({base_location.zipcode})"
