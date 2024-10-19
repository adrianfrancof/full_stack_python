* Crear carpeta
* crear entorno virtual

```
python -m venv .venv
```

* activar entorno virtual

```
.venv\Scripts\activate.ps1
```

* instalar django en el entorno si no éxiste

```
pip install Django==5.1.2
```

* crear proyecto django

```
django-admin startproject nombre_proyecto
```

* crear app dentro del proyecto

```
django-admin startapp nombre_app
```

* registrar cada app en el archivo settings.py que se encuentra deltro de la carpeta del proyecto

```
INSTALLED_APPS = [
    'app.apps.AppConfig',
]
```

* migrar los cambios a la base de datos

```
python manage.py migrate
```

* inicializar el servidor

```
python manage.py runserver
```

* terminar servidor

> ctrl + c

* verificación e instalacion de python

```
python --version
```

* verificacion de pip
  pip --version
* verificación e instalación de virtualenvwrapper
  https://pypi.org/project/virtualenvwrapper/
  https://pypi.org/project/virtualenvwrapper-win/
  https://virtualenvwrapper.readthedocs.io/en/latest/
  https://virtualenvwrapper.readthedocs.io/en/latest/install.html#supported-shells

```
pip install virtualenvwrapper
```

Run: workon
A list of environments, empty, is printed.

Run: mkvirtualenv temp
A new environment, temp is created and activated.

Run: workon
This time, the temp environment is included.
