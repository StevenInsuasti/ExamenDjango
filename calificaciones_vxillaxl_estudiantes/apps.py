from django.apps import AppConfig


class CalificacionesVxillaxlEstudiantesConfig(AppConfig):
    name = 'calificaciones_vxillaxl_estudiantes'

    def ready(self):
        from . import signals  # noqa: F401
