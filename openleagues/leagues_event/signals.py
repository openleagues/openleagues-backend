from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from openleagues.leagues_event.models import LeaguesEvent

# Signal to update spots when teams are added or removed
# @receiver(m2m_changed, sender=LeaguesEvent.teams.through)
# def update_spots(sender, instance, action, **kwargs):
#     if action in ['post_add', 'post_remove', 'post_clear']:
#         instance.update_active_spots()
#         instance.save()
