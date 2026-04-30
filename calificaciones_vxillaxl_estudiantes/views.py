from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.db.models import Avg
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CalificacionForm, LoginForm, RegistroUsuarioForm
from .models import Calificacion


class CustomLoginView(LoginView):
    template_name = "registration/login.html"
    authentication_form = LoginForm
    redirect_authenticated_user = True


def inicio(request):
    if request.user.is_authenticated:
        return redirect("listar_calificaciones")
    return render(request, "inicio.html")


def registro_usuario(request):
    if request.user.is_authenticated:
        return redirect("listar_calificaciones")
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Tu cuenta quedo creada correctamente.")
            return redirect("listar_calificaciones")
    else:
        form = RegistroUsuarioForm()
    return render(request, "registration/registro.html", {"form": form})




@login_required
def listar_calificaciones(request):
    calificaciones = Calificacion.objects.all().order_by("nombre_estudiante")
    promedio_general = calificaciones.aggregate(Avg("promedio"))["promedio__avg"]
    return render(
        request,
        "calificaciones/listar.html",
        {"calificaciones": calificaciones, "promedio_general": promedio_general},
    )


@login_required
def crear_calificacion(request):
    if request.method == "POST":
        form = CalificacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_calificaciones")
    else:
        form = CalificacionForm()
    return render(request, "calificaciones/crear.html", {"form": form})


@login_required
def editar_calificacion(request, pk):
    calificacion = get_object_or_404(Calificacion, pk=pk)
    if request.method == "POST":
        form = CalificacionForm(request.POST, instance=calificacion)
        if form.is_valid():
            form.save()
            return redirect("listar_calificaciones")
    else:
        form = CalificacionForm(instance=calificacion)
    return render(request, "calificaciones/editar.html", {"form": form, "calificacion": calificacion})


@login_required
def eliminar_calificacion(request, pk):
    calificacion = get_object_or_404(Calificacion, pk=pk)
    if request.method == "POST":
        calificacion.delete()
        return redirect("listar_calificaciones")
    return render(request, "calificaciones/eliminar.html", {"calificacion": calificacion})


@login_required
def promedio_general(request):
    promedio = Calificacion.objects.all().aggregate(Avg("promedio"))["promedio__avg"]
    return render(request, "calificaciones/promedio_general.html", {"promedio_general": promedio})
