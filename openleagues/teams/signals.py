from django.db.models.signals import post_save
from django.dispatch import receiver
from openleagues.authentication.models import User
from openleagues.teams.models import Team

@receiver(post_save, sender=User)
def create_default_team_for_user(sender, instance, created, **kwargs):
    if created:
        name = f"{instance.first_name} {instance.last_name}"
        new_team = Team.objects.create(name=name)
        new_team.members.add(instance)

        # Save the team to persist the relationship
        new_team.save()
