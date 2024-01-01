from django.contrib import admin
from django import forms
from openleagues.teams.models import Team
from openleagues.authentication.models import User

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = "__all__"
    
    name = forms.CharField()
    members = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

class TeamAdmin(admin.ModelAdmin):
    form = TeamForm
    model = Team

admin.site.register(Team, TeamAdmin)
