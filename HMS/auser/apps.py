from django.apps import AppConfig


class AuserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auser'
    icon = 'fa fa-user'
    
    def ready(self):
        from . import signals
