# login de un usuario
> https://docs.djangoproject.com/en/5.1/topics/auth/default/

* clonar el proyecto anterior o seguir trabajando en el mismo

* URL: crear url para capturar la petición de login
> app/urls.py

* VIEW: view para manejar la petición de login
> app/views.py
`from django.contrib.auth import authenticate, login, logout`

* TEMPLATE: template para renderizar formulario de login
> app/templates/login.html
> https://mdbootstrap.com/docs/standard/extended/login/

# redireccionamiento a página inicial cuando el login es correcto

* URL: crear url para capturar la petición de página inicial luego que se validan las credenciales del usuario
> app/urls.py

* VIEW: view para manejar la petición de página inicial luego que se validan las credenciales del usuario
> app/views.py

* SETTINGS: configurar el redireccionamiento a página inicial cuando el login es correcto
> proyecto/settings.py
`LOGIN_URL = /home/`

# cierre de sesión

* URL: crear url para capturar la petición de logout o cirre de sesión
> app/urls.py

* VIEW: view para manejar la petición de logout o cirre de sesión
> app/views.py

# Navbar
> templates/navbar.html
* agregar enlaces en la barra de navegación para registro, login, logout y home

# seguritizar los views
> app/views.py
`from django.contrib.auth.decorators import login_required`

* agregar decorator @login_required a las vistas que requieren autenticación
```
@login_required # para que solo se pueda acceder si esta logeado
def lista_libros(request):

@login_required    
def editar_libro(request, libro_id):

@login_required    
def eliminar_libro(request, libro_id):

@login_required
def cerrar_sesion(request):
```
