from django.db import models
# from openleagues.teams.models import Team
# from openleagues.leagues_event.models import LeaguesEvent
from .MatchScore import MatchScore

class Match(models.Model):
    team1 = models.ForeignKey("teams.Team", related_name='matches_as_team1', on_delete=models.CASCADE)
    team2 = models.ForeignKey("teams.Team", related_name='matches_as_team2', on_delete=models.CASCADE)
    leagues_event = models.ForeignKey("leagues_event.LeaguesEvent", related_name='matches', on_delete=models.CASCADE)
    score = models.OneToOneField(MatchScore, on_delete=models.CASCADE, null=True, blank=True)
    default_match = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
 
    def __str__(self):
        return f"Match between {self.team1.name} and {self.team2.name}"
