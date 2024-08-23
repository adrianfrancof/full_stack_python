'''
Set, conjunto de datos
no permite elementos repetidos
no mantiene un orden
se definen mediante la funcion set()
se definen con llaves
'''

miset = {} # set vacio
miset = set({1,2,1,2,1,3,4,5,6,7})
print(miset) # {1, 2, 3, 4, 5, 6, 7}

# longitud de un set
print('La longitud del conjunto es', len(miset))

# agregar un elemento al set
miset.add(8) # añade el elemento 8

# eliminar un elemento si existe
# miset.remove(10) # elimina el elemento 10 si existe si no KeyError: 10

# descartar elemento
miset.discard(2) # elimina el elemento 2 si existe

copy_miset = miset.copy()  # copia el set
print('La copia del conjunto es', copy_miset)

# ordenar un set
miset_ordenado = set(sorted(miset))
print('El conjunto ordenado es', miset_ordenado)

# eliminar todos los elementos
copy_miset.clear()   # elimina todos los elementos del set
print('La copia del conjunto es', copy_miset)

# añadir un elemento
copy_miset.add('un elemento agregado')
print('La copia del conjunto es', copy_miset)

# eliminar un elemento
copy_miset.remove('un elemento agregado')  # elimina el elemento si existe, si no ejecuta un error KeyError: 'un elemento agregado'

# actualizar
copy_miset.update({'otra vez'}) # añade otro elemento al set
print('La copia del conjunto es', copy_miset)

# unir
print('La union de los set es',miset.union(copy_miset))   # unión de los dos sets

# intersectar
set_interserccion = miset.intersection({1,2})  # intersección de los dos sets
print('La intersección de los set es', set_interserccion)

miset.intersection_update(copy_miset)    # actualiza el set con la intersección
print('El conjunto miset ahora es', miset)

# desempaquetar set
a = set_interserccion
print(f'a:{a}')
