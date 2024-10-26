* URL: crear path para la ruta editar_libro/
> app/urls.py
```
urlpatterns = [
    path('editar_libro/<int:libro_id>', editar_libro, name="editar_libro") # registrando ruta para editar libro
]
```

* Template: editar listar_libros.html y agregar boton para editar un libro que comunica con el path editar_libro/id

* View: crear una vista llamada editar_libro, que recibe un request y retorna el template book/editar_libro.html
> app/views.py
    * https://docs.djangoproject.com/en/5.1/topics/http/shortcuts/
    * https://www.geeksforgeeks.org/get_object_or_404-method-in-django-models/

* Template: crear una plantilla llamada editar_libro.html, que recibe el formulario del libro.
> app/templates/editar_libro.html

* Fontawsome: agregar icono para boton de guardar cambios en la vista editar_libro.
> https://fontawesome.com/

* activar entorno
`.\.venv\Scripts\activate.ps1`

* ejecutar servidor, ubicarse en la carpeta del proyecto donde se encuentra el archivo manage.py
`python manage.py runserver`