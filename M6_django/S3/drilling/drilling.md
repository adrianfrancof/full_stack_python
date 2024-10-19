* crear carpeta para almacenar el proyecto
`mkdir practica`

* ingresar a la carpeta creada
`cd practica`

* crear entorno virtual django_development
`python -m venv django_development`
`python -m venv django_development_1`

* activar entorno local
    * windows: `django_development\Scripts\activate.ps1`
    * linux: `source django_development/bin/activate`

* eliminar entorno
    * windows: `rm django_development_1`
    * linux: `rm -rf ~./django_development_1`

* instalar django 4.0.5
`pip install Django==4.0.5`
`python.exe -m pip install --upgrade pip`

* crear proyecto django
`django-admin startproject project`

* ubicarse en la carpeta del proyecto
`cd project`

* crear la app
`django-admin startapp app`

* registrar la aplicación en el archivo settings.py
>project/settings.py
```
INSTALLED_APPS = [
    'app.apps.AppConfig',
]
```
* realizar migración e inicialización de base de datos
`python manage.py migrate`

* inicializar servidor
 `python manage.py runserver`

    