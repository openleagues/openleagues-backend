from openleagues.teams.models import Team
from openleagues.teams.serializers import TeamSerializer
from rest_framework import generics

class TeamList(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
