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
        sets_data = validated_data.pop('sets', None)
        match_score = MatchScore.objects.create(**validated_data)
        
        if sets_data:
            for set_data in sets_data:
                SetScore.objects.create(match_score=match_score, **set_data)
        
        return match_score

class MatchSerializer(serializers.ModelSerializer):
    score = MatchScoreSerializer(required=False)

    class Meta:
        model = Match
        fields = '__all__'
    
    # def create(self, validated_data):
    #     score_data = validated_data.pop('score', None)
    #     match = Match.objects.create(**validated_data)
        
    #     if score_data:
    #         sets_data = score_data.pop('sets')
    #         match_score = MatchScore.objects.create(**score_data)
    #         for set_data in sets_data:
    #             SetScore.objects.create(match_score=match_score, **set_data)
        
    #     return match
