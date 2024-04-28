from django.db import models
from openleagues.authentication.models import User
from openleagues.matches.models import Match
from django.db.models import Sum
import uuid

class Team(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name='teams', blank=True)
    public = models.BooleanField(default=False)

    def __str__(self):
            return self.name

    def total_games_won(self, league_event):
        # Get all matches for the specified league event where the team participated
        matches = Match.objects.filter(leagues_event=league_event) | Match.objects.filter(leagues_event=league_event, team2=self)
        # Calculate total games won by the team in these matches
        total_won = 0
        for match in matches:
            if match.team1 == self:
                total_won += match.score.sets.all().aggregate(Sum('team1'))['team1__sum']
            elif match.team2 == self:
                total_won += match.score.sets.all().aggregate(Sum('team2'))['team2__sum']
        return total_won
