
from django.test import TestCase

from openleagues.matches._models import MatchScore, SetScore, Match
from openleagues.teams.models import Team
from openleagues_tests.factories import LeaguesEventFactory


class TeamTotalGamesWonTestCase(TestCase):
    def setUp(self):
        # Create teams
        self.team1 = Team.objects.create(name='Team 1')
        self.team2 = Team.objects.create(name='Team 2')

        # Create match scores
        match_score1 = MatchScore.objects.create()
        match_score2 = MatchScore.objects.create()

        # Create set scores
        set_score1 = SetScore.objects.create(team1=6, team2=4)
        set_score2 = SetScore.objects.create(team1=7, team2=5)

        self.leagues_event = LeaguesEventFactory(status="in-progress")

        # Assign set scores to match scores
        match_score1.sets.add(set_score1)
        match_score2.sets.add(set_score2)

        # Create matches
        self.match1 = Match.objects.create(team1=self.team1, team2=self.team2, score=match_score1, leagues_event=self.leagues_event)
        self.match2 = Match.objects.create(team1=self.team1, team2=self.team2, score=match_score2, leagues_event=self.leagues_event)

    def test_total_games_won(self):
        # Assert initial total games won for league event
        self.assertEqual(self.team1.total_games_won(league_event=self.leagues_event), 13)  # team1 won 13 games
        self.assertEqual(self.team2.total_games_won(league_event=self.leagues_event), 9)  # team2 won 9 games
