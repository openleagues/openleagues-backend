import pytest


def test_league_event_str(base_league_event):
    assert base_league_event.__str__() == f"{base_league_event.title}"

def test_location_str(base_location):
    assert base_location.__str__() == f"{base_location.county}, {base_location.state} ({base_location.zipcode})"
