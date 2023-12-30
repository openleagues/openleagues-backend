from rest_framework import serializers
from openleagues.teams.models import Team

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        exclude = ["id"]
