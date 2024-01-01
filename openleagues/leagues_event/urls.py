from django.urls import path
from openleagues.leagues_event import views

urlpatterns  = [
    path("", views.LeaguesEventList.as_view()),
    path("<uuid:id>/", views.LeaguesEventDetail.as_view()),
    path("locations/", views.LocationList.as_view()),
]
