from django.db import models
from openleagues.authentication.models import User

class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name='teams', blank=True)
    public = models.BooleanField(default=False)

    def __str__(self):
            return self.name
