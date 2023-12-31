from django.db import models
from .MatchFormat import MatchFormat
from .Location import Location
from openleagues.common.models import TimeStampedUUIDModel
from openleagues.authentication.models import User
from openleagues.teams.models import Team

GENDER_CHOICES = [
    ("M", "Male"),
    ("F", "Female"),
    ("Mixed", "Mixed"),
]

MINIMUM_LEVEL_CHOICES = [
    ("1.0", "1.0"),
    ("1.5", "1.5"),
    ("2.0", "2.0"),
    ("2.5", "2.5"),
    ("3.0", "3.0"),
    ("3.5", "3.5"),
    ("4.0", "4.0"),
    ("4.5", "4.5"),
    ("5.0", "5.0"),
    ("5.5", "5.5"),
    ("6.0", "6.0"),
]

STATUS = [
    ("open", "Open"),
    ("inprogress", "In Progress"),
    ("completed", "Completed"),
    ("cancelled", "Cancelled")
]

class LeaguesEvent(TimeStampedUUIDModel):

    class Meta:
        pass
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    start_week = models.DateField()
    end_week = models.DateField()
    description = models.TextField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    minimum_level = models.CharField(max_length=10, choices=MINIMUM_LEVEL_CHOICES)
    total_spots = models.PositiveIntegerField()
    active_spots = models.PositiveIntegerField(null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS, default="open")

    match_format = models.OneToOneField(MatchFormat, on_delete=models.CASCADE, related_name='+', null=True, blank=False)
    teams = models.ManyToManyField(Team, related_name='events')

    def __str__(self):
        return self.title  
