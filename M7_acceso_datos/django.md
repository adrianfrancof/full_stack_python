* Instalar postgres
* Instalar pgadmin
* Crear base de datos
`CREATE DATABASE DB_PRACTICA_ORM;`
* Crear usuario
`CREATE USER user_db WITH PASSWORD 'user_db';`

* Dar permisos al usuario
`GRANT ALL PRIVILEGES ON DATABASE DB_PRACTICA_ORM TO user_db;`
`GRANT ALL PRIVILEGES ON DATABASE DB_PRACTICA_ORM TO postgres;`

* Crear entorno virtual o usar éxistente
`python -m venv .venv`

* Instalar paquetes dentro del entorno
`pip install -r requirements.txt`
> django, django-bootstrap-v5, django-crispy-forms, crispy-bootstrap5, psycopg2

* Crear proyecto Django
`django-admin startproject config`
`cd config`

* crear aplicacion con Django
`django-admin startapp producto`

* Configurar settings.py para la conexión a base de datos

* Registrar aplicación en settings.py
```
INSTALLED_APPS = [
    'producto.apps.ProductoConfig',
]
```

* Realizar migraciones
`python manage.py migrate`

* Crear modelo Producto
```
class Producto(models.Model):
    nombre = models.TextField(max_length=50)
```    

* Registrar las url dentro de urls.py del proyecto
> config/urls.py
```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('producto.urls')),
    path('producto/', include('producto.urls'))
]
```
* Registrar paquetes django-bootstrap-v5, django-crispy-forms, crispy-bootstrap5 dentro de settings.py
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'producto.apps.ProductoConfig',
    'bootstrap5',
    'crispy_forms', # https://github.com/django-crispy-forms/crispy-bootstrap5
    'crispy_bootstrap5',
]


CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
```

* URL: crear archivo urls.py dentro del aplicativo
> producto/urls.py
```
from django.urls import path
from .views import listar_producto, crear_producto, editar_producto

urlpatterns = [
    path('', index, name='index'),
    path('listar_producto/', listar_producto, name='listar_producto'),
    path('crear_producto/', crear_producto, name='crear_producto'),
    path('editar_producto/<int:producto_id>', editar_producto, name='editar_producto'),
]
```
* MODELS: crear modelos dentro de models.py
```
class Producto(models.Model):
    nombre = models.TextField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField(max_length=100)
    fecha_vencimiento = models.DateField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(default=datetime.datetime.now())
    fecha_modificacion = models.DateTimeField(default=datetime.datetime.now())
    fabrica = models.ForeignKey(Fabrica, on_delete=models.CASCADE, blank=True, null=True)
    fabrica = models.ForeignKey(Fabrica, on_delete=models.SET_NULL, blank=True, null=True)
    fabrica = models.OneToOneField(Fabrica, on_delete=models.CASCADE, blank=True, null= True)
    fabrica = models.ManyToManyField(Fabrica)
```

* VIEWS: crear views dentro de views.py
> listar
```
def listar(request):
    productos = Producto.objects.all()
    return render(request, 'listar_productos.html', {'productos':productos})
```
> crear, editar
```
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto creado')
            return redirect('listar_producto')
        else:
            messages.error(request, 'Revisar datos ingresados')
            return HttpResponseRedirect(reverse('crear_producto'))
    else:
        form = ProductoForm()
        return render(request, 'crear_producto.html', {'producto_form':form}) 
```    

* FORMS: crear ProductoForm dentro de forms.py
>producto/forms.py
```
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'descripcion', 'fabrica']
        labels = {
            'nombre': 'Nombre del producto',
            'precio': 'Precio del producto',
            'descripcion': 'Descripción del producto',
            'fabrica': 'Fábrica del producto'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control','required': True}),
            'nombre': forms.TextInput(attrs={'class':'form-control','required': True}),
            'precio': forms.NumberInput(attrs={'class':'form-control', 'required': True}),
            'descripcion': forms.TextInput(attrs={'class':'form-control', 'required': True}),
            'fabrica': forms.Select(attrs={'class':'form-control', 'required': True})
        } 
```        

* TEMPLATES: crear templates para visualizar
> producto/templates/listar_productos.html
> producto/templates/crear_producto.html
> producto/templates/editar_producto.html

* crear clases que representen a los modelos dentro del admin.py
```
class FabricaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais')
    list_display_links = ['nombre', 'pais']
    list_filter = ('nombre', 'pais')

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'fecha_vencimiento', 'precio', 'fabrica')
    list_display_links = ['id', 'nombre']
    list_filter = ('nombre', 'fabrica')   
    
admin.site.register(Fabrica, FabricaAdmin)
admin.site.register(Producto, ProductoAdmin)
```

* crear superuser mediante manage.py, úbicarse en la terminal a la altura del archivo manage.py
`python manage.py createsuperuser`
