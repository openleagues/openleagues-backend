from rest_framework import serializers
from openleagues.matches.models import Match, MatchScore, SetScore

class MatchesPreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        include = ["team1", "team2", "score"]

class SetScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = SetScore
        fields = '__all__'

class MatchScoreSerializer(serializers.ModelSerializer):
    sets = SetScoreSerializer(many=True)

    class Meta:
        model = MatchScore
        fields = '__all__'
    
    def create(self, validated_data):
        # Extract sets data from validated data
        sets_data = validated_data.pop('sets')

        # Create MatchScore instance
        match_score = MatchScore.objects.create(**validated_data)

        # Create SetScore instances and associate with MatchScore
        for set_data in sets_data:
            set_score = SetScore.objects.create(**set_data)
            match_score.sets.add(set_score)

        return match_score


class MatchSerializer(serializers.ModelSerializer):
    score = MatchScoreSerializer(required=False)

    class Meta:
        model = Match
        fields = '__all__'
