# Generated by Django 4.2 on 2024-01-03 01:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('leagues_event', '0006_alter_leaguesevent_active_spots_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchFormat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_type', models.CharField(choices=[('singles', 'Singles'), ('doubles', 'Doubles'), ('mixed-doubles', 'Mixed Doubles')], max_length=25)),
                ('pro_set', models.BooleanField(default=False)),
                ('number_of_sets', models.PositiveIntegerField(default=1)),
                ('no_ad_scoring', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='leaguesevent',
            name='format',
        ),
        migrations.RemoveField(
            model_name='leaguesevent',
            name='team_type',
        ),
        migrations.AlterField(
            model_name='leaguesevent',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('Mixed', 'Mixed')], max_length=10),
        ),
        migrations.AlterField(
            model_name='leaguesevent',
            name='status',
            field=models.CharField(choices=[('open', 'Open'), ('inprogress', 'In Progress'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='open', max_length=15),
        ),
        migrations.AddField(
            model_name='leaguesevent',
            name='match_format',
            field=models.OneToOneField(default=999, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='leagues_event.matchformat'),
            preserve_default=False,
        ),
    ]
