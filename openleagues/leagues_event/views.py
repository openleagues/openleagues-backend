from openleagues.leagues_event.models import LeaguesEvent
from openleagues.leagues_event.serializer import LeaguesEventSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from openleagues.leagues_event.permissions import IsOwnerOrReadOnly

class LeaguesEventList(generics.ListCreateAPIView):
    queryset = LeaguesEvent.objects.all()
    serializer_class = LeaguesEventSerializer

class LeaguesEventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LeaguesEvent.objects.all()
    # Change serializer for more information
    serializer_class = LeaguesEventSerializer
    lookup_field = "id"
    #permission_classes = [IsAuthenticated]
