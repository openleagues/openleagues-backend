from django.apps import AppConfig


class LeaguesEventConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'openleagues.leagues_event'

    def ready(self):
        import openleagues.leagues_event.signals
