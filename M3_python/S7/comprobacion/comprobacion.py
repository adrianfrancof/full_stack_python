'''
Crear una lista con 10 números enteros, recorrerla haciendo uso de la sentencia for, e imprimir en pantalla el valor de cada elemento indicando si es par, impar o cero.
'''
lista = [0,100,20,5,7,10,30,70,6,2] # indices van de 0 a n-1

for i in lista:
    if i == 0:
        print(f'es cero {i}')
    elif i % 2 == 0:
        print(f'es par {i}')
    else: 
        print(f'es impar {i}')   