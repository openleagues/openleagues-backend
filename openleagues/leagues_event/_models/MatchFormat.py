from django.db import models

MATCH_TYPE_CHOICES = [
    ("singles", "Singles"),
    ("doubles", "Doubles"),
    ("mixed-doubles", "Mixed Doubles"),
]


class MatchFormat(models.Model):
    match_type = models.CharField(max_length=25, choices=MATCH_TYPE_CHOICES)
    pro_set = models.BooleanField(default=False)
    number_of_sets = models.PositiveIntegerField(default=1)
    no_ad_scoring = models.BooleanField(default=False)

    def __str__(self):
        return f"Match type: {self.match_type}, pro-set: {self.pro_set}, Number of sets: {self.number_of_sets} with no ad scoring: {self.no_ad_scoring}"
