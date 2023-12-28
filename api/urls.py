from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/leagues", include("openleagues.leagues_event.urls"))
]
