from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from openleagues.matches.models import Match, MatchScore, SetScore
from openleagues.matches.serializers import MatchesPreviewSerializer, MatchScoreSerializer
from django.db.models import Q
from rest_framework.response import Response

class MatchesView(generics.ListAPIView):
    serializer_class = MatchesPreviewSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        leagues_event_id = self.kwargs.get("league_event_id")

        queryset = Match.objects.filter(
            Q(team1__members=self.request.user) | Q(team2__members=self.request.user),
            leagues_event_id=leagues_event_id
        )

        return queryset

class MatchScoreUpdateView(generics.CreateAPIView):
    serializer_class = MatchScoreSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
                # Retrieve match instance based on match_id from path variable
        match_id = self.kwargs.get('match_id')
        try:
            match = Match.objects.get(id=match_id)
        except Match.DoesNotExist:
            return Response({"error": "Match not found."}, status=status.HTTP_404_NOT_FOUND)

        # Check if user is part of either team in the match
        if not (request.user in match.team1.members.all() or request.user in match.team2.members.all()):
            return Response({"error": "You are not a member of either team in the match."}, status=status.HTTP_403_FORBIDDEN)

        # Continue with serializer logic to create MatchScore
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # Add created MatchScore to the match
        match.score = serializer.instance
        match.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

