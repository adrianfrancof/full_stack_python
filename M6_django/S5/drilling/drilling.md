* copiar proyecto anterior o crear uno con todas las configuraciones necesarias

* eliminar templates
> book/templates/index.html
> book/templates/espalindromo.html

* eliminar métodos de views.py, solo dejar IndexPageView

* eliminar los path creados en urls.py de la aplicación book
solo dejar
```
urlpatterns = [
    path('', IndexPageView.as_view(),name="index"),
]
```

* estructura de templates a crear
base.html -> estructura base
	include: navbar.html -> barra de navegacion

layout.html -> template a reutilizar
	extends: base.html -> estructura base

index.html -> pagina principal
	extends: layout.html -> template a reutilizar

actores o archivos a crear:
navbar.html
base.html
layout.html
index.html

* activar el entorno o usar entorno global

* instalar en el entorno bootstrap 5
https://django-bootstrap5.readthedocs.io/en/latest/installation.html
pip install django-bootstrap-v5

* registrar el uso de bootstrap 5 como app en settings.py
```
INSTALLED_APPS = [
    'bootstrap5',
]
```

* crear archivo navbar.html dentro de la carpeta templates
> templates/navbar.html

* crear archivo base.html dentro de la carpeta templates
> templates/base.html

* crear archivo layout.html que extiende de base.html dentro de la carpeta templates
>templates/layout.html

* crear archivo index.html que extiende layout.html dentro de la carpeta templates
> templates/index.html