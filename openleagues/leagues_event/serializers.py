from rest_framework import serializers
from openleagues.leagues_event.models import LeaguesEvent, Location, MatchFormat
from openleagues.teams.serializers import TeamSerializer
from openleagues.authentication.serializers import UserMemberSerializer

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        exclude = ["id"]

class MatchFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchFormat
        exclude = ["id"]

class LeaguesEventSerializer(serializers.ModelSerializer):
    match_format = MatchFormatSerializer()

    class Meta:
        model = LeaguesEvent
        exclude = ["pkid", "updated_at", "teams"]

    def create(self, validated_data):
        match_format_data = validated_data.pop('match_format')
        match_format_instance = MatchFormat.objects.create(**match_format_data)

        leagues_event_instance = LeaguesEvent.objects.create(match_format=match_format_instance, **validated_data)
        return leagues_event_instance

class LeaguesEventDetailsSerializer(serializers.ModelSerializer):
    match_format = MatchFormatSerializer(read_only=True)
    location = LocationSerializer(read_only=True)
    teams = TeamSerializer(read_only=True, many=True)
    owner = UserMemberSerializer(read_only=True)

    active_players = serializers.SerializerMethodField()

    class Meta:
        model = LeaguesEvent
        exclude = ["pkid", "updated_at"]
    
    def get_active_players(self, obj):
        return sum(team.members.count() for team in obj.teams.all()) if obj.teams.exists() else 0
