from django.test import TestCase
from openleagues.authentication.models import User
from openleagues.matches.models import Match
from openleagues.matches.serializers import MatchSerializer
from openleagues.teams.models import Team
from openleagues_tests.factories import LeaguesEventFactory


class MatchModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(first_name="test", last_name="tester", username='test_user', email='test@example.com', password='test_password')
        self.team1 = Team.objects.create(name='Team 1')
        self.team2 = Team.objects.create(name='Team 2')
        self.leagues_event = LeaguesEventFactory()

    def test_create_match(self):
        match = Match.objects.create(team1=self.team1, team2=self.team2, leagues_event=self.leagues_event)
        
        # Check that the match is created with the correct data
        self.assertIsNotNone(match)
        self.assertEqual(match.team1, self.team1)
        self.assertEqual(match.team2, self.team2)
        self.assertEqual(match.leagues_event, self.leagues_event)
