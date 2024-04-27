from django.test import TestCase
from openleagues.matches.models import Match, SetScore, MatchScore
from openleagues.matches.serializers import MatchSerializer, MatchScoreSerializer
from openleagues.teams.models import Team
from openleagues_tests.factories import LeaguesEventFactory


class MatchScoreTestCase(TestCase):
    def test_match_score_serializer(self):
        # Sample data
        sample_data = {
            "sets": [
                {"team1": 6, "team2": 4},
                {"team1": 7, "team2": 5}
            ],
            "confirmation": True  # Adjust as needed
        }

        # Initialize serializer with sample data
        serializer = MatchScoreSerializer(data=sample_data)

        # Ensure serializer is valid
        self.assertTrue(serializer.is_valid())

        # Save serializer data to create a MatchScore instance
        match_score_instance = serializer.save()

        # Verify that MatchScore instance is created
        self.assertIsNotNone(match_score_instance)

        # Verify that associated SetScore instances are created
        self.assertEqual(match_score_instance.sets.count(), 2)

        # Verify the data of the first SetScore instance
        first_set_score = match_score_instance.sets.first()
        self.assertEqual(first_set_score.team1, 6)
        self.assertEqual(first_set_score.team2, 4)

        # Verify the data of the second SetScore instance
        second_set_score = match_score_instance.sets.last()
        self.assertEqual(second_set_score.team1, 7)
        self.assertEqual(second_set_score.team2, 5)

        # Verify confirmation flag of MatchScore instance
        self.assertTrue(match_score_instance.confirmation)
