from django.apps import AppConfig


class ChitchatConfig(AppConfig):
    name = 'chitchat'

    def ready(self):
        import chitchat.signals


