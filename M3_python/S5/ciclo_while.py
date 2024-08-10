# ciclo while, mientras que
# while condicion:

# i, j, k, temp, iterador, nombres para los iteradores

i = 0
while i < 5:
    i  += 1 # i = i + 1 aumentar el valor del iterador, para controlar el ciclo
    print(i)
    
i = 0
while i < 5:
    print(i)
    i += 1 # aumentar el valor del iterador, para controlar el ciclo
    
i = 0
while i < 5:
    print(i)
    i += 1 # aumentar el valor del iterador, para controlar el ciclo
    if i == 1:
        continue # salta a la siguiente iteración
    print(f'Imprimiendo el valor de {i}')    


i = 0
while i < 5:
    print(i)
    i += 1 # aumentar el valor del iterador, para controlar el ciclo
    if i == 4:
        break # termina el ciclo
    print(f'Imprimiendo el valor de {i}')      