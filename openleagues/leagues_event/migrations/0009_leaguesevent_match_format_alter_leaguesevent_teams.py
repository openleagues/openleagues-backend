# Generated by Django 4.2 on 2024-01-03 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0006_team_uid'),
        ('leagues_event', '0008_remove_leaguesevent_match_format'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaguesevent',
            name='match_format',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='leagues_event.matchformat'),
        ),
        migrations.AlterField(
            model_name='leaguesevent',
            name='teams',
            field=models.ManyToManyField(related_name='events', to='teams.team'),
        ),
    ]
