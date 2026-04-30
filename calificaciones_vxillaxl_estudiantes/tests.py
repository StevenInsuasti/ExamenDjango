from decimal import Decimal

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Calificacion


class CalificacionModelTest(TestCase):
    def test_calcula_promedio_automaticamente(self):
        calificacion = Calificacion.objects.create(
            nombre_estudiante="Ana Perez",
            identificacion="12345",
            asignatura="Matematicas",
            nota1=Decimal("4.0"),
            nota2=Decimal("3.5"),
            nota3=Decimal("5.0"),
        )
        self.assertEqual(calificacion.promedio, Decimal("4.17"))


class CalificacionViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="alumno", password="clave12345")

    def test_listado_requiere_login(self):
        response = self.client.get(reverse("listar_calificaciones"))
        self.assertEqual(response.status_code, 302)

    def test_listado_muestra_promedio_general(self):
        self.client.login(username="alumno", password="clave12345")
        Calificacion.objects.create(
            nombre_estudiante="Juan",
            identificacion="111",
            asignatura="Fisica",
            nota1=Decimal("3.0"),
            nota2=Decimal("4.0"),
            nota3=Decimal("5.0"),
        )
        response = self.client.get(reverse("listar_calificaciones"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "4")
