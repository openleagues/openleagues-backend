from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from openleagues.matches.models import Match
from openleagues.matches.serializers import MatchesPreviewSerializer
from django.db.models import Q

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

    
