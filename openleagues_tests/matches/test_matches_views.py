from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from openleagues.authentication.models import User
from openleagues.teams.models import Team
from openleagues.matches.models import Match, SetScore, MatchScore
from openleagues.leagues_event.models import LeaguesEvent
from rest_framework_simplejwt.tokens import AccessToken
from openleagues_tests.factories import LeaguesEventFactory, UserFactory


class MatchScoreCreateViewTestCase(TestCase):
    def setUp(self):
        # Create test user
        self.user = UserFactory()

        # Create LeagueEvent
        self.leagues_event = LeaguesEventFactory(status="in-progress")

        # Create teams and match
        self.team1 = Team.objects.create(name='Team 1')
        self.team2 = Team.objects.create(name='Team 2')
        self.match = Match.objects.create(team1=self.team1, team2=self.team2, leagues_event=self.leagues_event)

        # Create APIClient
        self.client = APIClient()

        # Obtain access token for test user
        access_token = AccessToken.for_user(self.user)
        self.headers = {'Authorization': f'Bearer {access_token}'}

    def test_create_match_score_happy_path(self):
        # Sample match score data
        match_score_data = {
            "sets": [
                {"team1": 6, "team2": 4},
                {"team1": 7, "team2": 5}
            ],
            "confirmation": True
        }

        self.team1.members.add(self.user)

        # Make POST request to create match score with access token in headers
        
        response = self.client.post(f'/api/v1/matches/{self.match.id}/update-score/', match_score_data, format='json', headers=self.headers)

        # Check response status code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if match score was created and associated with the match
        self.assertTrue(Match.objects.filter(id=self.match.id, score=response.data['id']).exists())
    
    def test_create_match_score_user_not_in_either_team(self):
        # Sample match score data
        match_score_data = {
            "sets": [
                {"team1": 6, "team2": 4},
                {"team1": 7, "team2": 5}
            ],
            "confirmation": True
        }

        # Make POST request to create match score with access token in headers
        
        response = self.client.post(f'/api/v1/matches/{self.match.id}/update-score/', match_score_data, format='json', headers=self.headers)

        # Check response status code
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data['error'], "You are not a member of either team in the match.")

