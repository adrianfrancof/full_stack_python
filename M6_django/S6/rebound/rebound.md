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

* Ruta: agregar al archivo urls.py dentro de la app, la estructura necesaria para listar los libros
> book/urls.py
```
urlpatterns = [
    path('', IndexPageView.as_view(),name="index"),
	path('lista_libros/', lista_libros, name='lista_libros')
]
```

* Controlador: en el archivo views.py agregar una función que despliegue una lista de libros

* Model: crear un modelo para los libros
> https://docs.djangoproject.com/en/5.1/topics/db/models/
> https://www.w3schools.com/django/django_models.php
```
class Book(models.Model):
    # atributos
    titulo = models.CharField(max_length = 100, null = False)
    autor = models.CharField(max_length = 50, null = False)
    valoracion = models.IntegerField(help_text = 'Valoración entre 0 y 100')
```

* Template: crear template, crear un archivo html para listar los libros
> templates/lista_libros.html
```
{% extends 'layout.html' %}

{% block content %}
    <section class="container mt-5">
        <h2>Lista Libros</h2>
        {% if libros %}
        <!-- tabla con libros -->
        <table class="table table-striped">
          <thead>
            <tr>
              <th scope="col">ID</th>
              <th scope="col">Titulo</th>
              <th scope="col">Autor</th>
              <th scope="col">Valoración</th>
            </tr>
          </thead>
          <tbody>
          {% for libro in libros %}
            <tr>
              <td>{{ libro.id }}</td>
              <td>{{ libro.titulo }}</td>
              <td>{{ libro.autor }}</td>
              <td>{{ libro.valoracion }}</td>
            </tr>
          {% empty %}
            <tr>
                <td colspan="4">No hay libros disponibles</td>
            </tr>
          {% endfor %}
          </tbody>
        </table>
        {% else %}
        <!-- No hay libros -->
        <p>No hay libros disponibles</p>
        {% endif %}

    </section>
{% endblock %}
```

* Realizar migraciones
`python manage.py makemigrations book`
`python manage.py sqlmigrate book 0001`
`python manage.py migrate`
