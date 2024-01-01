from rest_framework import serializers
from openleagues.teams.models import Team

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class UserAddRemoveSerializer(serializers.Serializer):
    user_id = serializers.UUIDField()
