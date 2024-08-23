'''
1. Eliminar los elementos duplicados.
2. Ordenar la lista resultante en orden ascendente.
La lista es: 1 mi_lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15]
'''

mi_lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15]
lista_sin_duplicado = []
for item in mi_lista:
    if item not in lista_sin_duplicado:
        lista_sin_duplicado.append(item)
       
print(lista_sin_duplicado)

#----------------------------------------------------------------------------

mi_lista2 = []
mi_lista2 = mi_lista[0:1]
for i in range(len(mi_lista)):
    if mi_lista[i] not in mi_lista2:
        mi_lista2.append(mi_lista[i])
    print(mi_lista2)
    
#----------------------------------------------------------------------------
mi_lista = list(set(mi_lista)).sort()
mi_lista = sorted(list(set(mi_lista)))