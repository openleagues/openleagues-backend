from django.db import models
from openleagues.authentication.models import User


class Team(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name='teams', blank=True)

    def __str__(self):
            return self.name
    def __unicode__(self):
        return self.name
