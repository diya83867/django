from django.apps import AppConfig


class ChannelappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'channelapp'

    def ready(self):
        import channelapp.signals