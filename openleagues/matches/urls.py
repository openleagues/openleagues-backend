from django.urls import path
from openleagues.matches.views import MatchesView

urlpatterns = [
    # Other URL patterns
    path('<uuid:league_event_id>/', MatchesView.as_view(), name='matches-list'),
]
