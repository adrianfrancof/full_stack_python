# Base de datos // diccionario vacio
inventario = {}
 
#Funcion de agregar producto al inventario
def agregar_producto (nombre, cantidad, precio):
    inventario[nombre] = {"cantidad": cantidad, "precio": precio}
 
#Funcion de eliminar producto del inventario
def eliminar_producto(nombre):
    if nombre in inventario:
        del inventario[nombre]
    else :
        print("El producto no existe en el inventario ")
 
#Funcion de actualizar producto del inventario
def actualizar_producto(nombre, cantidad, precio):
    if nombre in inventario:
        inventario[nombre] = {"cantidad": cantidad, "precio": precio}
    else:
        ("El producto no existe en el inventario")
 
def ver_inventario():
    for clave, valor in inventario.items():
        print(f"Producto :{clave}, Cantidad: {valor['cantidad']}, Precio: {valor['precio']}" )
       
def valor_total_inventario():
    total = sum(detalles['cantidad'] * detalles['precio'] for detalles in inventario.values())
    return total       
 
def ingreso_opcion():
    return input('Ingrese una Opcion: \n'
                 + '1.- agregar\n'
                 + '2.- eliminar\n'
                 + '3.- actualizar\n'
                 + '4.- ver inventario\n'
                 + '5.- valor total del inventario\n'
                 + '6.- salir\n')
   
def ingreso_valores_productos():    
    nombre = input('ingrese el nombre: ')
    cantidad = ingreso_numero('ingrese el cantidad: ')  
    precio = ingreso_numero('ingrese el precio: ')    
    return (nombre, cantidad, precio)
 
def ingreso_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print('Opción invalida, ingrese un número')
 
   
def menu():
     while True:
        opcion_ingresada = ingreso_opcion()
        #match opcion_ingresada:
        if opcion_ingresada == '1':
            nombre,cantidad,precio = ingreso_valores_productos()
            agregar_producto(nombre,cantidad,precio)
        elif opcion_ingresada== '2':
            nombre_producto =  input("Ingrese el nombre del producto")
            eliminar_producto(nombre_producto)
        elif opcion_ingresada== '3':
            nombre,cantidad,precio = ingreso_valores_productos()
            actualizar_producto(nombre,cantidad,precio)
        elif opcion_ingresada == '4':
            ver_inventario()
        elif opcion_ingresada == '5':
            valor_total_inventario()   
        elif opcion_ingresada == '6':
            break
        else:
            print("Opcion invalida")
 
menu()