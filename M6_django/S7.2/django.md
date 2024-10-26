* URL: crear path para la ruta eliminar_libro/
> app/urls.py
```
urlpatterns = [
    path('eliminar_libro/<int:libro_id>', eliminar_libro, name="eliminar_libro") # registrando ruta para editar libro
]
```

* Template: editar lista_libros.html y agregar boton para eliminar un libro que comunica con el path eliminar_libro/id

* Fontawesome: agregar icono para boton de guardar cambios en la vista listar_libros.html
> https://fontawesome.com/

* View: crear una vista llamada eliminar_libro, que recibe un request y retorna el template book/editar_libro.html
> app/views.py
    * https://docs.djangoproject.com/en/5.1/topics/http/shortcuts/
    * https://www.geeksforgeeks.org/get_object_or_404-method-in-django-models/

# Mensajes: agregar mensajes de confirmacion
> app/views.py
importar librerias para mensaje
`from django.contrib import messages`

importar librerias HttResponseRedirect
`from django.http import HttpResponseRedirect`

importar librerias para reverse
`from django.urls import reverse`

* templates: agregar en los templates el tag para desplegar mensajes mediante django.contrib.messages
    * Display django.contrib.messages as Bootstrap alerts `{% bootstrap_messages %}`

* views: módificar los views para desplegar los mensajes necesarios de acuerdo al resultado de la operación    

* activar entorno
`.\.venv\Scripts\activate.ps1`

* ejecutar servidor, ubicarse en la carpeta del proyecto donde se encuentra el archivo manage.py
`python manage.py runserver`