from django.db import models
from openleagues.authentication.models import User
import uuid

class Team(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name='teams', blank=True)
    public = models.BooleanField(default=False)

    def __str__(self):
            return self.name
