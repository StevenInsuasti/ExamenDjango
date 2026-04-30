from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import (
    CustomLoginView,
    crear_calificacion,
    editar_calificacion,
    eliminar_calificacion,
    inicio,
    listar_calificaciones,
    registro_usuario,
    promedio_general,
)

urlpatterns = [
    path("", inicio, name="inicio"),
    path("registro/", registro_usuario, name="registro"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("calificaciones/", listar_calificaciones, name="listar_calificaciones"),
    path("calificaciones/crear/", crear_calificacion, name="crear_calificacion"),
    path("calificaciones/<int:pk>/editar/", editar_calificacion, name="editar_calificacion"),
    path("calificaciones/<int:pk>/eliminar/", eliminar_calificacion, name="eliminar_calificacion"),
    path("promedio-general/", promedio_general, name="promedio_general"),
]
