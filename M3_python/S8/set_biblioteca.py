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

# libros que aún no han sido devueltos.
# buscar las diferencias entre un set y otro
libros_sin_devolver =  libros_prestados.difference(libros_devueltos)
print(libros_sin_devolver) 

# diferencias simetricas entre los set, y la contra parte es ^
libros_sin_devolver =  libros_prestados.symmetric_difference(libros_devueltos)
print(libros_sin_devolver)

# diferencias simetricas entre los set, contra parte de symmetric_difference()
libros_sin_devolver = libros_prestados ^ libros_devueltos
print(libros_sin_devolver)

libros_sin_devolver =  libros_devueltos.symmetric_difference(libros_prestados)
print(libros_sin_devolver)

# busca diferencias en el set mas largo, si no sabemos cual es, utilizar ^
libros_sin_devolver = libros_prestados - libros_devueltos
print(libros_sin_devolver)

