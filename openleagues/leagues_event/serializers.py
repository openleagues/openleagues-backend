from rest_framework import serializers
from openleagues.leagues_event.models import LeaguesEvent, Location

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        exclude = ["id"]

class LeaguesEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaguesEvent
        exclude = ["pkid", "updated_at", "teams"]
    
