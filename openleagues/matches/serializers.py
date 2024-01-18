from rest_framework import serializers
from openleagues.matches.models import Match

class MatchesPreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        include = ["team1", "team2", "score"]

