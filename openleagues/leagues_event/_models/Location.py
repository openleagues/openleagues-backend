from django.db import models

class Location(models.Model):
    state = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.county}, {self.state} ({self.zipcode})"
