from django.apps import AppConfig


class DProfileConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "d_profile"

    def ready(self):
        import d_profile.signals
