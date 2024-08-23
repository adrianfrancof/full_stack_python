'''
Se solicita crear un programa en Python que permita llevar el registro 
de los libros que han sido prestados por una biblioteca. 
Para ello, se pide crear un conjunto (set) con los nombres de los libros 
prestados.

A continuación, se solicita imprimir en pantalla la cantidad total de libros
prestados.

Finalmente, se debe crear otro conjunto con los nombres de los libros 
que han sido devueltos y mostrar en pantalla los libros que aún no han sido
devueltos. 

libros_prestados = {'Cien años de soledad', 'El amor en los tiempos del cólera', 'La ciudad y los perros', 'La casa verde', 'El otoño del patriarca', 'Rayuela', 'Pedro Páramo', 'La tregua'}
'''

# un conjunto (set) con los nombres de los libros prestados.
libros_prestados = {'Cien años de soledad', 'El amor en los tiempos del cólera', 'La ciudad y los perros', 'La casa verde', 'El otoño del patriarca', 'Rayuela', 'Pedro Páramo', 'La tregua', 'Quien se robo mi queso'}

# imprimir en pantalla la cantidad total de libros prestados.
print('Libros prestados', len(libros_prestados))

# conjunto con los nombres de los libros que han sido devueltos
libros_devueltos = {'Python machine learning', 'Python para dummies', 'Papelucho', 'El principito', 'Cien años de soledad'}

# opcion = input()
# opcion = opcion.lower()
# opcion = opcion.strip()
while True:
    
    opcion = input('''
               Bienvenido
               Que desea realizar?
               a) consultar libros prestados
               b) agregar libros devueltos
               s) salir
               ''').lower().strip()
    
    base_actualizada_libros = libros_prestados.difference(libros_devueltos)
    
    match opcion:
        case 'a' | 'consultar':
            print('La cantidad de libros prestados es:', len(base_actualizada_libros))
            print('Falta por devolver:', base_actualizada_libros)
        case 'b' | 'agregar' :
            print('Falta por devolver:', base_actualizada_libros)
            libro_devuelto = input('''Ingrese el libro a devolver:''').strip()
            libros_devueltos.add(libro_devuelto)
        case 's' | 'salir':
            print('adios')
            break
        case _ :
            print('opción invalida, ingrese otra opción')     
            

