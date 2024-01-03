from openleagues.leagues_event.models import LeaguesEvent, Location
from openleagues.leagues_event.serializers import LeaguesEventSerializer, LeaguesEventDetailsSerializer, LocationSerializer
from rest_framework import generics
from rest_framework.validators import ValidationError

class LeaguesEventList(generics.ListCreateAPIView):
    queryset = LeaguesEvent.objects.all()
    serializer_class = LeaguesEventSerializer

    def perform_create(self, serializer):
        owner = serializer.validated_data.get('owner')
        title = serializer.validated_data.get('title')
        start_date = serializer.validated_data.get('start_week')
        end_date = serializer.validated_data.get('end_week')

        # Check for existing events with the same attributes
        existing_events = LeaguesEvent.objects.filter(
            owner=owner,
            title=title,
            start_week__lte=end_date,
            end_week__gte=start_date
        )
        if existing_events.exists():
            message = "Event has already been created"
            raise ValidationError(message)

        # Proceed with creating the new event if no duplicates are found
        serializer.save()

class LeaguesEventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LeaguesEvent.objects.all()
    # Change serializer for more information
    serializer_class = LeaguesEventDetailsSerializer
    lookup_field = "id"

class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
