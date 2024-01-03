from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from openleagues.leagues_event.models import LeaguesEvent

# Signal to update active spots when teams are added or removed
# @receiver(m2m_changed, sender=LeaguesEvent.teams.through)
# def update_active_spots(sender, instance, **kwargs):
#     instance.update_active_spots()
