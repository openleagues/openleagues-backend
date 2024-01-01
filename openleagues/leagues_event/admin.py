from django.contrib import admin
from django import forms
from openleagues.leagues_event.models import LeaguesEvent
from openleagues.leagues_event.models import Location

class LeaguesEventForm(forms.ModelForm):
    class Meta:
        model = LeaguesEvent
        fields = "__all__"

class LeaguesEventAdmin(admin.ModelAdmin):
    form = LeaguesEventForm


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = "__all__"

class LocationAdmin(admin.ModelAdmin):
    form = LocationForm
    list_display = [
        "id",
        "state",
        "city",
        "zipcode",
    ]

admin.site.register(LeaguesEvent, LeaguesEventAdmin)
admin.site.register(Location, LocationAdmin)
