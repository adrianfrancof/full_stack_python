1. Crear la carpeta template.
> book/template/

2. Proceder a crear nuestro archivo index.html. 
> book/templates/index.html
* `html:5`
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Bienvenido a mi sitio de libros</h1>
</body>
</html>
```

3. Adecuar la vista views.py.
> crear en book/views.py
```
class IndexPageView(TemplateView):
    template_name = 'index.html'
```

4. Configuración del Path /URLs.
> book/urls.py
```
urlpatterns = [
    # path('', views.index, name='index'),
    path('', IndexPageView.as_view(),name="index"),
]
```

5. Configurar con la finalidad de que la página de inicio del proyecto se redireccione a la página index, previamente creada.