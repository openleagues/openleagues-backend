# Generated by Django 4.2 on 2023-12-31 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leagues_event', '0004_leaguesevent_teams'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leaguesevent',
            old_name='spots',
            new_name='total_spots',
        ),
        migrations.AddField(
            model_name='leaguesevent',
            name='active_spots',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
