from openleagues.leagues_event.models import LeaguesEvent, Location
from openleagues.leagues_event.serializers import LeaguesEventSerializer, LocationSerializer
from rest_framework import generics

class LeaguesEventList(generics.ListCreateAPIView):
    queryset = LeaguesEvent.objects.all()
    serializer_class = LeaguesEventSerializer

class LeaguesEventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LeaguesEvent.objects.all()
    # Change serializer for more information
    serializer_class = LeaguesEventSerializer
    lookup_field = "id"

class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
