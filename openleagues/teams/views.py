from openleagues.teams.models import Team
from openleagues.teams.serializers import TeamSerializer, UserAddRemoveSerializer
from openleagues.authentication.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class TeamList(generics.ListCreateAPIView):
    serializer_class = TeamSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        return Team.objects.filter(members=user)


class UserAddToTeamView(generics.UpdateAPIView):
    queryset = Team.objects.all()
    lookup_field = "uid"

    def update(self, request, *args, **kwargs):
        team = self.get_object()
        # For now return error, but later request access to join from current team members if public is False
        if not team.public:
            return Response({'detail': 'This team is not public. New users cannot join.'}, status=status.HTTP_403_FORBIDDEN)
        
        user = request.user
        team.members.add(user)

        return Response(TeamSerializer(team).data, status=status.HTTP_200_OK)

class UserRemoveFromTeamView(generics.UpdateAPIView):
    queryset = Team.objects.all()
    lookup_field = "uid"

    def update(self, request, *args, **kwargs):
        team = self.get_object()
        user = request.user
        team.members.remove(user)
        return Response(TeamSerializer(team).data, status=status.HTTP_200_OK)
