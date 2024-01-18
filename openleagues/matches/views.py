from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from openleagues.matches.models import Match
from openleagues.matches.serializers import MatchesPreviewSerializer

class TeamMatchesView(generics.ListAPIView):

    queryset = Match.objects.all()
    serializer_class = MatchesPreviewSerializer
