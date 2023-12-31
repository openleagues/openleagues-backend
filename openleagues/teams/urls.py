from django.urls import path
from openleagues.teams import views

urlpatterns  = [
    path("", views.TeamList.as_view()),
    path("add/", views.UserAddToTeamView.as_view()),
    path("remove/", views.UserRemoveFromTeamView.as_view()),
]
