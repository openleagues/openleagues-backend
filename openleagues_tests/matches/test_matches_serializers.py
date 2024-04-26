from django.test import TestCase
from openleagues.matches.models import Match, SetScore, MatchScore
from openleagues.matches.serializers import MatchSerializer
from openleagues.teams.models import Team
from openleagues_tests.factories import LeaguesEventFactory


class MatchSerializerTestCase(TestCase):
    def setUp(self):
        # Create sample SetScore instances
        set_score1 = SetScore.objects.create(team1=6, team2=4)
        set_score2 = SetScore.objects.create(team1=7, team2=5)

        # Create a sample MatchScore instance with SetScore instances
        match_score = MatchScore.objects.create(confirmation=False)
        match_score.sets.add(set_score1, set_score2)
        leagues_event = LeaguesEventFactory(status="in-progress")
        team1 = Team.objects.create(name='Team 1')
        team2 = Team.objects.create(name='Team 2')
        # Create a sample Match instance with MatchScore
        self.match = Match.objects.create(team1_id=1, team2_id=2, leagues_event_id=1, score=match_score)

    def test_match_serializer_from_models(self):
        serializer = MatchSerializer(instance=self.match)
        serialized_data = serializer.data

        # Assert that serialized data matches expected data
        self.assertEqual(serialized_data['team1'], self.match.team1_id)
        self.assertEqual(serialized_data['team2'], self.match.team2_id)
        self.assertEqual(serialized_data['leagues_event'], self.match.leagues_event_id)
        self.assertEqual(serialized_data['score']['confirmation'], self.match.score.confirmation)

        # Assert that the nested sets are serialized correctly
        serialized_sets = serialized_data['score']['sets']
        self.assertEqual(len(serialized_sets), 2)
        self.assertEqual(serialized_sets[0]['team1'], 6)
        self.assertEqual(serialized_sets[0]['team2'], 4)
        self.assertEqual(serialized_sets[1]['team1'], 7)
        self.assertEqual(serialized_sets[1]['team2'], 5)
    
    # def test_match_serializer(self):
        # # Sample data representing an API request body
        # request_body = {
        #     "team1": 1,
        #     "team2": 2,
        #     "leagues_event": 1,
        #     "score": {
        #         "sets": [
        #             {"team1": 6, "team2": 4},
        #             {"team1": 7, "team2": 5}
        #         ],
        #         "confirmation": False
        #     }
        # }

        # # Initialize MatchSerializer with the request body
        # serializer = MatchSerializer(data=request_body)

        # # Validate and save the serializer
        # if serializer.is_valid():
        #     # Save the serialized data (if needed)
        #     match_instance = serializer.save()
            
        #     # Assert the serialized data
        #     self.assertEqual(serializer.data['team1'], request_body['team1'])
        #     self.assertEqual(serializer.data['team2'], request_body['team2'])
        #     self.assertEqual(serializer.data['leagues_event'], request_body['leagues_event'])
        #     self.assertEqual(serializer.data['score']['confirmation'], request_body['score']['confirmation'])

        #     # Assert the nested sets are serialized correctly
        #     serialized_sets = serializer.data['score']['sets']
        #     self.assertEqual(len(serialized_sets), 2)
        #     self.assertEqual(serialized_sets[0]['team1'], 6)
        #     self.assertEqual(serialized_sets[0]['team2'], 4)
        #     self.assertEqual(serialized_sets[1]['team1'], 7)
        #     self.assertEqual(serialized_sets[1]['team2'], 5)
        # else:
        #     # If serializer validation fails, print errors
        #     print(serializer.errors)
