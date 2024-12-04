#* Conectar a la shell de python a la altura del archivo manage.py
# `python manage.py shell`

# https://docs.djangoproject.com/en/5.1/topics/db/queries/#complex-lookups-with-q
# https://www.w3schools.com/django/django_queryset.php
#1. Obtenga todos los registros de fábricas y productos.
from producto.models import Producto, Fabrica

productos = Producto.objects.all().values() # SELECT * FROM producto_producto;
fabricas = Fabrica.objects.all().values() # SELECT * FROM producto_fabrica;

productos
fabricas

#2. Obtenga los campos de nombre, precio, y fecha de vencimiento de los productos. Demuestre también cuál es la consulta SQL que se genera del ORM.
consulta1 = productos.values_list('nombre', 'precio', 'fecha_vencimiento')
consulta1

str(consulta1.query)
'SELECT "producto_producto"."nombre", "producto_producto"."precio", "producto_producto"."fecha_vencimiento" FROM "producto_producto"'


# 3. Obtenga los productos donde el precio sea menor o igual a 2500, mostrando solo los campos de nombre y precio, respectivamente. Demuestra también cuál es la consulta SQL que se genera del ORM.
consulta2 = productos.filter(precio__lte=2500).values('nombre', 'precio')
consulta2
str(consulta2.query)
'SELECT "producto_producto"."nombre", "producto_producto"."precio" FROM "producto_producto" WHERE "producto_producto"."precio" <= 2500'

consulta3 = productos.filter(precio__gte=2500).values('nombre', 'precio')
consulta3
str(consulta3.query)
'SELECT "producto_producto"."nombre", "producto_producto"."precio" FROM "producto_producto" WHERE "producto_producto"."precio" >= 2500'

# 4. Consulte los productos que se vencen antes del año 2024, e imprima el nombre, precio, fecha_vencimiento, y fabricante. Demuestre también cuál es la consulta SQL que se genera del ORM.
consulta4 = productos.filter(fecha_vencimiento__lte='2023-12-1').values('nombre', 'precio', 'fecha_vencimiento', 'fabrica')
consulta4
str(consulta4.query)
'SELECT "producto_producto"."nombre", "producto_producto"."precio", "producto_producto"."fecha_vencimiento", "producto_producto"."fabrica_id" FROM "producto_producto" WHERE "producto_producto"."fecha_vencimiento" <= 2023-12-01'

consulta5 = productos.filter(fecha_vencimiento__gte='2023-12-1').values('nombre', 'precio', 'fecha_vencimiento', 'fabrica')
consulta5
str(consulta5.query)
'SELECT "producto_producto"."nombre", "producto_producto"."precio", "producto_producto"."fecha_vencimiento", "producto_producto"."fabrica_id" FROM "producto_producto" WHERE "producto_producto"."fecha_vencimiento" >= 2023-12-01'

producto_1 = Producto.objects.select_related('fabrica').get(id=2)
productos_list = Producto.objects.select_related('fabrica').all()
producto_nombre = Producto.objects.select_related('fabrica').get(id=2).nombre

producto_1.nombre
producto_1.id
producto_1.precio