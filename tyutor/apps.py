from django.apps import AppConfig


class TyutorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tyutor'

    def ready(self):
        import tyutor.signals