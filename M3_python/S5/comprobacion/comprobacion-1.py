'''
Requerimos calcular el factorial de un número, asignarlo a una variable, y luego imprimirla. 
Sabiendo que el factorial es el resultado de la multiplicación de todos los enteros positivos 
que hay entre un número y uno. Ejemplo: Factorial de 4 es 4 * 3 * 2 * 1.
'''

while True:
    n = int(input('Ingrese el numero del que desea saber el factorial: '))
    if n > 0:
        break
    
# n puede tener cualquier valor positivo y mayor a 0
# el factorial es el resultado de la multiplicación de todos los enteros positivos 
# que hay entre un número y uno
i = 1 # iterador
acumulador = 1 # acumula el valor del factorial, la multiplicación del acumulador * i
while True:
    acumulador *= i # acumulador = acumulador * i, 1 = 1 * 1, 1 = 1 * 2
    i += 1 # iterador cambia valor
    if i > n:
        break
    
print(f'El factorial de {n} es {acumulador}')

# convertir estructura a ciclo for
    