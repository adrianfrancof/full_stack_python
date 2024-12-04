# 1. Obtener todas las fábricas y productos por medio de una consulta SQL, haciendo uso del método raw(). Para los productos imprima la fábrica correspondiente.
# python manage.py shell

from producto.models import Producto, Fabrica

fabricas = Fabrica.objects.raw('SELECT * FROM producto_fabrica')
for f in fabricas:
    print(f.nombre)


productos = Producto.objects.raw('SELECT * FROM producto_producto')
for p in productos:
    if p.fabrica is not None:
        print(f'{p.nombre} es fabricado por {p.fabrica.nombre}')
    else:
        print(f'No tiene fabrica asignada')    


# 2. Realizar una consulta pasando los parámetros por raw que busque el producto “Protex Aloe”, y devuelva quien lo fabrica.

producto = 'Protex Aloe'
productos_encontrados = Producto.objects.raw('SELECT * FROM producto_producto WHERE nombre = %s', [producto])
for p in productos_encontrados:
    if p.fabrica is not None:
        print(f'{p.nombre} es fabricado por {p.fabrica.nombre}')
    else:
        print(f'No tiene fabrica asignada') 

