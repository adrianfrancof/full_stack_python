# pytho manage.py shell
from producto.models import Producto, Fabrica

# 1. Obtenga los campos de nombre, precio, y fecha de vencimiento de los productos. 
# El producto: Colgate 360 se vence en 2024-02-29, con un precio de: 1850.00.
# https://docs.djangoproject.com/en/5.1/topics/db/sql/
consulta1 = Producto.objects.raw('SELECT id, nombre, precio FROM producto_producto')
print('\n'.join(str(i)) for i in consulta1)
for p in consulta1:
    print(f'El producto: {p.nombre} se vence en {p.fecha_vencimiento}, con un precio de: {p.precio}')


# 2. Obtenga los productos donde el precio sea menor o igual a 2500, y muestre solo los campos de nombre y precio, respectivamente.
# El producto: Colgate 360 tiene un precio de: 1850.00.
consulta2 = Producto.objects.raw('SELECT id, nombre, precio FROM producto_producto WHERE precio <= %s', [2500])
for p in consulta2:
    print(f'El producto: {p.nombre} tiene un precio de: {p.precio}')

# 3. Modifique haciendo uso de SQL personalizado y cursores, la fábrica con nombre P&G en el país que se encuentra asignada a EEUU, o a Canadá.
# https://docs.djangoproject.com/en/5.1/topics/db/sql/#:~:text=The%20object%20django.db.connection%20represents%20the%20default%20database%20connection.,cursor.fetchone%28%29%20or%20cursor.fetchall%28%29%20to%20return%20the%20resulting%20rows.
from django.db import connection


def my_custom_sql():
    with connection.cursor() as cursor:
        cursor.execute("UPDATE producto_fabrica SET pais = %s WHERE nombre = %s", ['EEUU', 'P&G'])
        cursor.execute("UPDATE producto_fabrica SET pais = %s WHERE nombre = %s", ['Canada', 'Colgate'])
        cursor.execute("SELECT * FROM producto_fabrica")
        row = cursor.fetchall()
    return row

row = my_custom_sql()



# Obtenga los productos cuyo nombre contiene la palabra 'Aloe' y muestre solo los campos de nombre y precio.

# Obtenga los productos que se vencen antes del año 2025 y muestre solo los campos de nombre, precio y fecha de vencimiento.

# Actualice el precio de todos los productos fabricados por 'Colgate' a 3000.