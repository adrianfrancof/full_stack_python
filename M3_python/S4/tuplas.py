# tuplas
# Estructura de datos inmutable
# Se declaran con ()
# los indices van desde 0 a n-1

tupla_datos = () # tupla vacía
print(type(tupla_datos)) # <class 'tuple'>

tupla_datos = (1, 2, 3, 4, 5) # reasingación de valor
print(tupla_datos) # (1, 2, 3, 4, 5)

cuenta = tupla_datos.count(1)
print(cuenta) # 1

indice_del_valor = tupla_datos.index(5)
print(indice_del_valor) # 4


contenido_indice_cero = tupla_datos[0] # acceder a un elemento mediante su índice