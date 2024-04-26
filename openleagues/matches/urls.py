from django.urls import path
from openleagues.matches.views import MatchesView, MatchScoreUpdateView

urlpatterns = [
    # Other URL patterns
    path('<uuid:league_event_id>/', MatchesView.as_view(), name='matches-list'),
    path('<int:match_id>/update-score/', MatchScoreUpdateView.as_view(), name='match-score-update')

]
