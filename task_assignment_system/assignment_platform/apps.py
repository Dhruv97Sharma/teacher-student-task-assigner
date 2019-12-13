from django.apps import AppConfig


class AssignmentPlatformConfig(AppConfig):
    name = 'assignment_platform'

    def ready(self):
        import assignment_platform.signals