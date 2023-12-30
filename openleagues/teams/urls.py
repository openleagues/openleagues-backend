from django.urls import path
from openleagues.teams import views

urlpatterns  = [
    path("", views.TeamList.as_view()),
]
