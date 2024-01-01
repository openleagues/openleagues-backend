from rest_framework import serializers
from openleagues.teams.models import Team
from openleagues.authentication.serializers import UserMemberSerializer

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        exclude = ["id"]

    members = UserMemberSerializer(many=True, read_only=True)

class UserAddRemoveSerializer(serializers.Serializer):
    user_id = serializers.UUIDField()
