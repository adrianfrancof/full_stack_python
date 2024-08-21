'''
Son colecciones de datos que se pueden modificar
El acceso a los elementos de una tupa es por indice
Se definen con parentesis ()
Se pueden definir con la funcion tuple()
Se pueden definir con comas, pero no se recomienda
'''
tupla = tuple()
tupla = ()
num = 1,2,3,4,5
print(tupla)
print(num)

# indices van desde 0 a n-1
# permite indices negativos
tupla = (40, 1.80, 'Fulanito', 'Perez')

# acceder a la longitud de la tupla
print('La longitud de la tupla es', len(tupla))

# acceder a un elemento mediante el indice
print('El primer elemento es', tupla[0])
print('El ultimo elemento es', tupla[-1])

# contar elementos existentes en una tupla
print('Elementos numero 40 existentes', tupla.count(40))

# obtener el indice de un elemento
print('El indice del elemento 40', tupla.index(40)) # 1

# desempaquetar tuplas
# Genera error ValueError: too many values to unpack, si existen menos o mas elementos que variables
a, b, c, d, e = num

# a = num[0]
print(f'a:{a}, b:{b}')

# crear una tupla de otra tupla
# otra_tupla = tupla
          # (40, 1.80, 'Fulanito', 'Perez')  
sub_tupla = tupla[0:3]
print('Sub tupla', sub_tupla)
print(tupla[2:]) # desde el indice 2 hasta el final
print(tupla[:-1])  # desde el principio hasta el penultimo
print(tupla[0:4:2])  # desde el indice 0 hasta el indice 3, con saltos de 2 en 2

# [inicio:final:paso]
# (inicio,final,paso)