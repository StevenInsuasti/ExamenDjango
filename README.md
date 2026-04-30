# InicioDeSesion - Laboratorio Django

Proyecto de laboratorio en Django para gestionar calificaciones de estudiantes.

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

- `/`
- `/registro/`
- `/login/`
- `/calificaciones/`
- `/calificaciones/crear/`
- `/calificaciones/<id>/editar/`
- `/calificaciones/<id>/eliminar/`
- `/promedio-general/`
