'''
Adivinador de números
'''

import random

print("Debes adivinar un número secreto entre 1 y 100 antes de que la cuenta regresiva al azar llegue a 0 o serás electrocutado.")

azar2 = random.randint(1,100)

while True:
    azar = random.randint(0, 20)
    num = int(input("Elige un número: "))
    if num == azar2:
        print("¡Excelente! Encontraste el número secreto.")
        break
    elif num < azar2:
        print("El número secreto es mayor.")    
        if azar == 0:
            print('La cuenta llegó a 0 \n"Bzzzzzt". Moriste.')
            break
        else:
            print("La cuenta regresiva al azar va en",azar)
        
    elif num > azar2:
        print("El número secreto es menor.")
        if azar == 0:
            print('La cuenta llegó a 0 \n"Bzzzzzt". Moriste.')
            break
        else:
            print("La cuenta regresiva al azar va en",azar)