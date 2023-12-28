from rest_framework import serializers
from openleagues.leagues_event.models import LeaguesEvent

class LeaguesEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaguesEvent
        exclude = ["pkid", "updated_at"]
