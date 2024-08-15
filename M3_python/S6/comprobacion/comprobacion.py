'''
Escribir un programa que analice un número, e indique si es positivo o negativo, y si es par o impar. En caso de ser cero, también indicarlo. Se debe usar la expresión if-elif-else, y no usar subcondiciones; en su lugar, usar condiciones anidadas.
'''

# ingreso del numero
num = int(input('Ingrese un número'))

# verificar el numero

if num == 0 :
    print('El numero es cero')
elif num > 0 :
    if num % 2 == 0 :
        print('El numero es positivo y par')
    else :
        print('El numero es positivo e impar')
else:
    if num % 2 == 0 :
        print('El numero es negativo y par')
    else :
        print('El numero es negativo e impar')