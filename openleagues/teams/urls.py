from django.urls import path
from openleagues.teams import views

urlpatterns  = [
    path("", views.TeamList.as_view()),
    path("<uuid:uid>/join/", views.UserAddToTeamView.as_view()),
    path("<uuid:uid>/leave/", views.UserRemoveFromTeamView.as_view()),
    path("<uuid:league_event_id>/", views.LeagueEventTeamList.as_view()),
]
