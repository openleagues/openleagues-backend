from rest_framework import serializers
from openleagues.teams.models import Team
from openleagues.authentication.serializers import UserMemberSerializer
from openleagues.authentication.models import User

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        exclude = ["id"]

    members = serializers.ListField(
        child=serializers.UUIDField(),  # Assume a list of UUIDs for members
        write_only=True
    )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request', None)

        if request and request.method == 'GET' or request == "POST":
            # Customize 'members' field for GET requests
            data['members'] = UserMemberSerializer(instance.members.all(), many=True).data

        return data

    def create(self, validated_data):
        print("HELLO---------------")
        members_data = validated_data.pop('members', [])
        team = Team.objects.create(**validated_data)

        # Add members to the team using UUIDs
        for member_uuid in members_data:
            user = User.objects.get(id=member_uuid)
            print("DEFINETLY SHOULD HAVE ADDED")
            team.members.add(user)

        return team

class UserAddRemoveSerializer(serializers.Serializer):
    user_id = serializers.UUIDField()
