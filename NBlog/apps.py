from django.apps import AppConfig


class NblogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'NBlog'

    def ready(self):
        import NBlog.signals
