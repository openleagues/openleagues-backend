from openleagues.teams.models import Team
from openleagues.teams.serializers import TeamSerializer, UserAddRemoveSerializer
from openleagues.authentication.models import User
from openleagues.leagues_event.models import LeaguesEvent
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import Http404


class TeamList(generics.ListCreateAPIView):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

class LeagueEventTeamList(generics.ListCreateAPIView):
    serializer_class = TeamSerializer

    def get_queryset(self):
        league_event_id = self.kwargs.get('league_event_id')
        league_event = LeaguesEvent.objects.filter(id=league_event_id).first()
        # Filter teams by league event ID and whether they are public
        if not league_event:
            raise Http404()
        queryset = league_event.teams.filter(public=True)
        return queryset
    
class UserAddToTeamView(generics.UpdateAPIView):
    queryset = Team.objects.all()
    lookup_field = "uid"
    permission_classes = (IsAuthenticated, )

    def update(self, request, *args, **kwargs):
        team = self.get_object()
        # For now return error, but later request access to join from current team members if public is False
        if not team.public:
            return Response({'detail': 'This team is not public. New users cannot join.'}, status=status.HTTP_403_FORBIDDEN)
        
        user = request.user
        team.members.add(user)

        return Response({"data":TeamSerializer(team).data, "message":"Successfully joined a team"}, status=status.HTTP_200_OK)

class UserRemoveFromTeamView(generics.UpdateAPIView):
    queryset = Team.objects.all()
    lookup_field = "uid"

    def update(self, request, *args, **kwargs):
        team = self.get_object()
        user = request.user
        team.members.remove(user)
        return Response({"data":TeamSerializer(team).data, "message":"Successfully left a team"}, status=status.HTTP_200_OK)
