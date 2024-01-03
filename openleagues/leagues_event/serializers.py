from rest_framework import serializers
from openleagues.leagues_event.models import LeaguesEvent, Location, MatchFormat

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        exclude = ["id"]

# class MatchFormatSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MatchFormat
#         fields = '__all__'
    
# class LeaguesEventSerializer(serializers.ModelSerializer):
#     match_format = MatchFormatSerializer
#     class Meta:
#         model = LeaguesEvent
#         exclude = ["pkid", "updated_at", "teams"]

#     def create(self, validated_data):
#         match_format_data = validated_data.pop('match_format')
#         match_format_instance = MatchFormat.objects.create(**match_format_data)

#         leagues_event_instance = LeaguesEvent.objects.create(match_format=match_format_instance, **validated_data)
#         return leagues_event_instance
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
