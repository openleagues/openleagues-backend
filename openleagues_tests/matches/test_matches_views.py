from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from openleagues.authentication.models import User
from openleagues.teams.models import Team
from openleagues.matches.models import Match, SetScore, MatchScore
from openleagues.leagues_event.models import LeaguesEvent
from rest_framework_simplejwt.tokens import AccessToken
from openleagues_tests.factories import LeaguesEventFactory


class AddMatchScoreViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='test_user', first_name="test", last_name="tester", email='test@example.com', password='test_password')
        self.team1 = Team.objects.create(name='Team 1')
        self.team2 = Team.objects.create(name='Team 2')
        self.team1.members.add(self.user)  # Add the user to team1
        self.leagues_event = LeaguesEventFactory(status="in-progress")
        self.match = Match.objects.create(team1=self.team1, team2=self.team2, leagues_event=self.leagues_event)
        self.set_score_data = {'team1': 6, 'team2': 4}
        self.match_score_data = {'sets': [self.set_score_data], 'confirmation': False}

        self.access_token = AccessToken.for_user(self.user)

    def test_add_match_score_as_team_member(self):
        # Authenticate the user
        self.client.force_login(self.user)

        # Include the token in the request's Authorization header
        headers = {'Authorization': f'Bearer {self.access_token}'}

        # Send a POST request to add match score
        response = self.client.post(f'/api/v1/matches/{self.match.id}/update-score/', self.match_score_data, format='json', headers=headers)
        print(response.data)

        # Check that the response status code is 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_add_match_score_without_authentication(self):
    #     # Send a POST request without authenticating the user
    #     response = self.client.post(f'/matches/{self.match.id}/update-score/', self.match_score_data, format='json')

    #     # Check that the response status code is 401 Unauthorized
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # def test_add_match_score_as_non_team_member(self):
    #     # Create a new user who is not a member of either team
    #     new_user = User.objects.create_user(first_name="newtest", last_name="newtester", username='new_user', email='new@example.com', password='new_password')

    #     # Authenticate the new user
    #     self.client.force_login(new_user)

    #     # Send a POST request to add match score
    #     response = self.client.post(f'/matches/{self.match.id}/update-score/', self.match_score_data, format='json')

    #     # Check that the response status code is 403 Forbidden
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
