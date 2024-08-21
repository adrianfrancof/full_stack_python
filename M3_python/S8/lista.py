'''
lista, colecciones de datos.
lista, tambien llamados arreglos, son conjuntos ordenados de elementos.
se definen [] con corchetes
se definen con la funcion list()
'''
lista = [1, 2, 3, 4, 5, 6] #indices van desde 0 a n-1
otra_lista = [] # lista vacia
otra_lista = list() # lista vacia
otra_lista = [40, 1.80, 'Fulanito', 'Perez'] #listas de diferentes tipos de datos

# acceder a la longitud de la lista
print('La longitud de la lista es ', len(lista))
print('La longitud de la lista es ', len(otra_lista))

# conocer el tipo de dato
print(type(lista)) # <class 'list'>

# acceder a los elementos de la lista
print('El elemento dentro del indice 0 es ', lista[0]) # 1
print('El elemento dentro del indice -1 es', otra_lista[-1]) # 'Perez'

# agregar elemento al final de la lista
lista.append(7) # agregar un elemento al final de la lista
print('Elementos que se encuentran en la lista', lista) # [1, 2, 3, 4, 5, 6, 7]

# contar un elemento existente dado en la lista
print('La cuenta de elementos numero 3 existente es', lista.count(3))

print('El indice de Perez es', otra_lista.index('Perez'))  # 2

# insertar un elemento en la lista en un indice dado
lista.insert(6, 8) # agregar un elemento en el indice 6
print('Elementos que se encuentran en la lista',lista) # [1, 2, 3, 4, 5, 6, 8, 7]
lista.insert(-2, 7)
lista.insert(-1, 8)
print('Elementos que se encuentran en la lista',lista)

# eliminar un elemento de la lista
lista.remove(8) # remover el primer elemento encontrado con el valor dado
print('Elementos que se encuentran en la lista',lista)

suma_lista = lista + otra_lista
print(suma_lista)

# revertir la lista
lista.reverse()
print('La lista invertida es', lista)

# ordenar la lista
lista.sort()
print('La lista ordenada es', lista)
lista.sort(reverse=True)  # reverse=True para ordenar de forma descendente
print('La lista ordenada es', lista)

lista_ordenada = sorted(lista)
print('La lista ordenada es', lista_ordenada)

# desempaquetar una lista, tiene que ser la misma cantidad de variables que elementos de la lista
# Genera error ValueError: too many values to unpack, si existen menos o mas elementos que variables
edad, altura, nombre, apellido = otra_lista # [40, 1.80, 'Fulanito', 'Perez']

# edad = otra_lista[0]
print('La edad es', edad)
print('La altura es', altura)
print('El nombre es', nombre)
print('El apellido es', apellido)