* crear carpeta
* crear el entorno
  `python -m venv .venv`
* activar entorno
  `.\.venv\Scripts\activate.ps1`
* instalar django
  `pip install django`
* crear proyecto
  `django-admin startproject site_django`
* ingresar a la carpeta del proyecto creado
* crear aplicativo
  `django-admin startapp book`
* registrar aplicativo n settings.py

```
INSTALLED_APPS = [
    'book.apps.BookConfig',
]
```

* migrar base de datos
  `python manage.py migrate `
* incluir las urls aceptadas por el aplicativo en urls.py del proyecto

```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', include('book.urls')),
    path('', include('book.urls'))
]
```

* crear urls del aplicativo, crear el archivo urls.py en book

> book/urls.py

```
urlpatterns = [
    path('', views.index, name='index'),
]
```

* crear en el archivo views.py el método index

```
def index(request):
    return HttpResponse('<h1>Bienvenido a mi sitio de libros</h1>')
```
