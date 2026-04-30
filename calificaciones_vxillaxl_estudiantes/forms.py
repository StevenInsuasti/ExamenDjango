from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import Calificacion


class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        exclude = ("promedio",)
        widgets = {
            "nombre_estudiante": forms.TextInput(attrs={"class": "form-control"}),
            "identificacion": forms.TextInput(attrs={"class": "form-control"}),
            "asignatura": forms.TextInput(attrs={"class": "form-control"}),
            "nota1": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "nota2": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "nota3": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Usuario",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Usuario"}),
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Contraseña"}),
    )


class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(
        label="Correo",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "correo@ejemplo.com"}
        ),
    )
    first_name = forms.CharField(
        label="Nombre",
        max_length=150,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre"}),
    )
    last_name = forms.CharField(
        label="Apellido",
        max_length=150,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Apellido"}),
    )

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")
        widgets = {
            "username": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre de usuario"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Contraseña"}
        )
        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Confirmar contraseña"}
        )
