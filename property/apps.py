from django.apps import AppConfig


class PropertyConfig(AppConfig):
    name = "property"

    def ready(self):
        from property import signals
