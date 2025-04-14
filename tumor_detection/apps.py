from django.apps import AppConfig


class TumorDetectionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tumor_detection'
    
    def ready(self):
        import tumor_detection.templatetags.form_tags
