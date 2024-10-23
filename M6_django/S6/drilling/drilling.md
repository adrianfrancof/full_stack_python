* URL: crear path para la ruta crear_libro/
> app/urls.py

* View: crear una vista llamada crear_libro, que recibe un request y retorna el template book/crear_libro.html
> app/views.py

* Formulário: crear un formulario para la creación de libros.
> app/forms.py

* Template: crear una plantilla llamada crear_libro.html, que recibe el formulario del libro.
> app/templates/crear_libro.html

* activar entorno
`.\.venv\Scripts\activate.ps1`

* ejecutar servidor, ubicarse en la carpeta del proyecto donde se encuentra el archivo manage.py
`python manage.py runserver`

* crear template footer.html
> app/templates/footer.html

* incluirlo en base.html