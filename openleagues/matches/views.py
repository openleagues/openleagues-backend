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
    queryset = Match.objects.all()
    serializer_class = MatchScoreSerializer
    #permission_classes = (IsAuthenticated, )

    def create(self, request, *args, **kwargs):
         # Get the match instance based on the URL parameter or any other method you use to retrieve it
        match_id = kwargs.get('match_id')
        match = Match.objects.get(id=match_id)

        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return Response({'error': 'Authentication credentials were not provided.'}, status=status.HTTP_401_UNAUTHORIZED)

        # Check if the user is a member of either of the teams in the match
        if request.user not in match.team1.members.all() and request.user not in match.team2.members.all():
            return Response({'error': 'You are not a member of either team in this match.'}, status=status.HTTP_403_FORBIDDEN)

        # Serialize and validate the request data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # # Save the match score
        # match_score = serializer.save()

        # # Associate the match score with the match
        # match.score = match_score
        # match.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

