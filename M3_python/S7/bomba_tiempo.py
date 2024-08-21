'''
Bomba de tiempo
Enunciado: Escribe un programa que permita la simulación de una bomba de tiempo. Al ejecutar el programa, se imprimirá el mensaje "Bomba del tiempo a explotar" 
'''
import time

def input_tiempo():
    while True :
        print('Bomba del tiempo a explotar')
        try:
            i = int(input('Ingrese el tiempo de explosión: '))
            if i > 0 :
                return i
        except ValueError as e:
            print('Error, ingrese un número entero')

def bomba_tiempo(i):    
    while i >= 0 :
        print(i)
        i -= 1
        time.sleep(1)
    print('boom')

bomba_tiempo(input_tiempo())