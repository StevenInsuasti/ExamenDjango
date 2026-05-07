from django.urls import path
from django.views.generic import TemplateView

app_name = "reservas"

urlpatterns = [
    path("", TemplateView.as_view(template_name="reservas/inicio.html"), name="inicio"),
]
