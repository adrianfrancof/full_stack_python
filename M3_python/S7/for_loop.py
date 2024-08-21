# while expreesion_evaluar:
#     secuencia de acciones

# for variable_temporal in secuencia:
#     accion_a_realizar

'''
for loop con listas
'''
mi_lista = [1, 2, 3, 4, 5]
for temp in mi_lista :
    print('Recorriendo la lista y obteniendo el elemento ' , temp)
    
mi_lista = [1, 2, 3, 4, 5]
for temp in mi_lista :
    print('Recorriendo la lista y obteniendo el indice del elemento' , mi_lista.index(temp))

mi_lista = [1, 2, 3, 4, 5]
for temp in range(len(mi_lista)) :
    print('Recorriendo la lista y obteniendo el indice del elemento' , temp)    
    
'''
for loop con tuplas
'''
mi_tupla = (1, 2, 3, 4, 5)
for temp in mi_tupla :
    print('Recorriendo la tupla y obteniendo el elemento ', temp)

for temp in range(len(mi_tupla)) :
    print('Recorriendo la tupla y obteniendo el indice ', temp)
    
'''
for loop con set o conjuntos
'''
mi_set = {1, 2, 3, 4, 5}
for temp in mi_set :
    print('Recorriendo el set y obteniendo el elemento ', temp)
    
mi_set = {1, 2, 3, 4, 5}
for temp in range(len(mi_set)) :
    print('Recorriendo el set y obteniendo el indice ', temp)
    
'''
for loop con diccionarios
'''
mi_diccionario = {'a': 1, 'b': 2, 'c' : 3, 'd' : 4, 'e' : 5}
for temp in mi_diccionario :
    print('Recorriendo el diccionario y obteniendo la llave ', temp)
    
mi_diccionario = {'a': 1, 'b': 2, 'c' : 3, 'd' : 4, 'e' : 5}
for key, value in mi_diccionario.items() :
    print(f'Recorriendo el diccionario y obteniendo la llave {key} y el valor {value}')

mi_diccionario = {'a': 1, 'b': 2, 'c' : 3, 'd' : 4, 'e' : 5}
for temp in mi_diccionario.values() :
    print('Recorriendo los valores del diccionario ', temp)
    
mi_diccionario = {'a': 1, 'b': 2, 'c' : 3, 'd' : 4, 'e' : 5}
for temp in mi_diccionario.keys() :
    print('Recorriendo las llaves del diccionario ', temp)                
