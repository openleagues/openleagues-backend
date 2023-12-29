from django.urls import path
from openleagues.leagues_event import views

urlpatterns  = [
    path("", views.leagues_event_list, name="get_league_events_list")
]
