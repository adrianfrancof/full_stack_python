'''
Requerimos calcular el factorial de un número, asignarlo a una variable, y luego imprimirla. 
Sabiendo que el factorial es el resultado de la multiplicación de todos los enteros positivos 
que hay entre un número y uno. Ejemplo: Factorial de 4 es 4 * 3 * 2 * 1.
'''
import math

while True:
    n = int(input('Ingrese un número:'))
    if n > 0:
        break

factorial = math.factorial(n)

print(f'El factorial del número {n} es {factorial}')