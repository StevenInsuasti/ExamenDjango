from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver


@receiver(post_migrate)
def crear_roles(sender, **kwargs):
    if sender.name != "calificaciones_vxillaxl_estudiantes":
        return

    editor_group, _ = Group.objects.get_or_create(name="Editor")
    cliente_group, _ = Group.objects.get_or_create(name="Cliente")

    permisos_editor = Permission.objects.filter(
        codename__in=[
            "view_calificacion",
            "add_calificacion",
            "change_calificacion",
            "delete_calificacion",
        ]
    )
    permisos_cliente = Permission.objects.filter(codename__in=["view_calificacion"])

    editor_group.permissions.set(permisos_editor)
    cliente_group.permissions.set(permisos_cliente)
