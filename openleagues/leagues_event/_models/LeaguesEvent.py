from django.db import models
from openleagues.leagues_event.models import Location
from openleagues.common.models import TimeStampedUUIDModel
import uuid
FORMAT_CHOICES = [
        ("singles", "Singles"),
        ("doubles", "Doubles"),
        ("mixed", "Mixed"),
    ]

TEAM_TYPE_CHOICES = [
    ("team", "Team"),
    ("individual", "Individual"),
]

GENDER_CHOICES = [
    ("M", "Male"),
    ("F", "Female"),
    ("all", "All"),
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
    ("cancelled", ("Cancelled"))
]

class LeaguesEvent(TimeStampedUUIDModel):

    class Meta:
        pass
    
    title = models.CharField(max_length=255)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    start_week = models.DateField()
    end_week = models.DateField()
    format = models.CharField(max_length=10, choices=FORMAT_CHOICES)
    team_type = models.CharField(max_length=15, choices=TEAM_TYPE_CHOICES)
    description = models.TextField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    minimum_level = models.CharField(max_length=10, choices=MINIMUM_LEVEL_CHOICES)
    spots = models.PositiveIntegerField()
    status = models.CharField(max_length=15, choices=STATUS)

    def __str__(self):
        return self.title
