from django.db import models

class SetScore(models.Model):
    team1 = models.PositiveIntegerField()
    team2 = models.PositiveIntegerField()

    def __str__(self):
        return f"Set: {self.team1}-{self.team2}"

class MatchScore(models.Model):
    sets = models.ManyToManyField(SetScore)
    confirmation = models.BooleanField(default=False)

    def __str__(self):
        return ", ".join(str(set_score) for set_score in self.sets)
