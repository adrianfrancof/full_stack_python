# set
# set de datos o conjunto de datos, es una estructura de datos que no permite duplicados
# se pueden realizar operaciones de conjuntos como unión, intersección, diferencia, etc.
# se utilizan {} para declarar un set de datos

# declarar variables
# snake_case = variable_uno
# camelCase = variableUno
variable_uno = 8 # int
variable_dos = 10.5 # float
variable_tres = 'ejercicio' #str

# crear set de datos
set_datos = {variable_uno, variable_dos, variable_tres}

lista_datos = [set_datos, False]

print(f'Lista de datos: {lista_datos}')

# uso de metodos de los set o conjuntos
set_datos.add(5) # agregar un elemento al set
print(set_datos) # {8, 10.5, 5, 'ejercicio'}

set_datos.remove('ejercicio') # eliminar un elemento del set
print(set_datos) # {8, 10.5, 5}

set_datos_copy = set_datos.copy() # copiar el set

set_datos_copy.clear() # limpiar el set
print(set_datos_copy)

set_datos.difference_update({8, 10.5}) # eliminar los elementos que coincidan con el set

interseccion_datos = set_datos.intersection(set_datos_copy) # intersección de dos sets
print(interseccion_datos)