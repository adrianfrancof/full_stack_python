* Trabajar con el proyecto anterior o clonar el proyecto

* verificar la instalación de auth y session en settings.py que se encuentra dentro del proyecto

* URL: crear url para captar petición o request para el registro de usuarios
> app/urls.py
```
urlpatterns = [
    # path(ruta, view, name=nombre_de_la_ruta)
    path('registro/', registro, name='registro')
]
```

* VIEWS: crear la vista para el registro de usuarios
> app/views.py
* importar UserCreationForm
    `from django.contrib.auth.forms import UserCreationForm`

* crear función de registro de usuario

* TEMPLATES: crear los templates para el registro de usuarios
    * Instalar paquete django-crispy-forms para renderizar los formularios
    * https://django-crispy-forms.readthedocs.io/en/latest/crispy_tag_forms.html
    `pip install django-crispy-forms`
    * Instalar paquete para que django-crispy-forms renderice los formularios usando bootstrap
    `pip install crispy-bootstrap5`

* crear el template para registro de usuarios
> templates/registro.html

* registrar las aplicaciones o paquetes instalados en settings.py
> proyecto/settings.py
```
INSTALLED_APPS = [
    'crispy_forms', # registro de crispy forms en el proyecto
    'crispy_bootstrap5', # registro de crispy bootstrap5 en el proyecto
]

# https://github.com/django-crispy-forms/crispy-bootstrap5
# https://django-crispy-forms.readthedocs.io/en/latest
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'
```

