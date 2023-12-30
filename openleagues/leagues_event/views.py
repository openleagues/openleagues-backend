from openleagues.leagues_event.models import LeaguesEvent
from openleagues.leagues_event.serializers import LeaguesEventSerializer
from rest_framework import generics

class LeaguesEventList(generics.ListCreateAPIView):
    queryset = LeaguesEvent.objects.all()
    serializer_class = LeaguesEventSerializer

class LeaguesEventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LeaguesEvent.objects.all()
    # Change serializer for more information
    serializer_class = LeaguesEventSerializer
    lookup_field = "id"
