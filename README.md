# InicioDeSesion - Laboratorio Django

Proyecto de laboratorio con Django para gestionar calificaciones de estudiantes, incluyendo:

- Autenticacion de usuarios (login/logout)
- Roles por grupos (Editor y Cliente)
- CRUD completo de `Calificacion`
- Calculo automatico del promedio individual
- Visualizacion del promedio general con `Avg`
- Interfaz con Bootstrap y estilos personalizados

## Estructura requerida

- Proyecto: `evaluaciones_vxillaxl_estudiantes`
- App: `calificaciones_vxillaxl_estudiantes`

## Instalacion

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Rutas principales

- `/login/`
- `/calificaciones/`
- `/calificaciones/crear/`
- `/calificaciones/<id>/editar/`
- `/calificaciones/<id>/eliminar/`
- `/promedio-general/`

## Roles

- **Editor**: ver, crear, editar y eliminar calificaciones.
- **Cliente**: solo puede ver el listado.

Los grupos se crean automaticamente al ejecutar migraciones.
