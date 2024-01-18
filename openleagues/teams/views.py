from openleagues.teams.models import Team
from openleagues.teams.serializers import TeamSerializer, UserAddRemoveSerializer
from openleagues.authentication.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class TeamList(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (IsAuthenticated, )


class UserAddToTeamView(generics.UpdateAPIView):
    serializer_class = UserAddRemoveSerializer
    queryset = Team.objects.all()
    lookup_field = "uid"

    def update(self, request, *args, **kwargs):
        team = self.get_object()
        # For now return error, but later request access to join from current team members if public is False
        if not team.public:
            return Response({'detail': 'This team is not public. New users cannot join.'}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_id = serializer.validated_data['user_id']

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        team.members.add(user)

        return Response(TeamSerializer(team).data, status=status.HTTP_200_OK)

class UserRemoveFromTeamView(generics.UpdateAPIView):
    serializer_class = UserAddRemoveSerializer
    queryset = Team.objects.all()
    lookup_field = "uid"

    def update(self, request, *args, **kwargs):
        team = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_id = serializer.validated_data['user_id']

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        team.members.remove(user)
        return Response(TeamSerializer(team).data, status=status.HTTP_200_OK)
