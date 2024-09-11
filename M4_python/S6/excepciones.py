# Exception: Clase base para todas las excepciones definidas en Python.
# AttributeError: Se produce cuando un objeto no tiene un atributo válido.
# TypeError: Se produce cuando se utiliza un tipo de dato incorrecto o inapropiado.
# ValueError: Se produce cuando se pasa un argumento con un valor inapropiado.
# NameError: Se produce cuando se utiliza un nombre que no está definido en el contexto actual.
# IndexError: Se produce cuando se intenta acceder a un índice de lista fuera de rango.
# KeyError: Se produce cuando se intenta acceder a una clave de diccionario que no existe.
# ZeroDivisionError: Se produce cuando se intenta dividir un número por cero.
# FileNotFoundError: Se produce cuando un archivo no puede ser encontrado.
# IOError: Se produce cuando hay un problema de entrada/salida en un archivo o en la consola.
# KeyboardInterrupt: Se produce cuando el usuario interrumpe la ejecución del programa (presionando Ctrl + C en la consola).
# StopIteration: Se produce cuando el método next() de un iterador no tiene más elementos para devolver.

# Exception >> ArithmeticError >> ZeroDivisionError

'''
Las excepciones pueden ocurrir al momento transformación de datos, lectura de archivos, asignación de variables, buscar un indice no existente, evaluando una variable, comunicación con un ente externo, en la interpretación del código.

Clase Exception: Clase base para todas las excepciones definidas en Python.
'''

def division():
    try:
        div = 10/0
    except ZeroDivisionError as e:
        print('ha ocurrido un error')
        
# division()

def division_multiple_exception():
    try:
        div = 10/0
        
    except Exception as error:
        print(error)
    # cuando éxiste una Excepcion mas general a la especifica primero la especifica no debe ir        
    except ZeroDivisionError as e:     
        print('ha ocurrido un error')
        
# division_multiple_exception()

def division_multiple_exception():
    try:
        div = 10/0
    
    # las excepciones expecificas deben ir primero a las excepciones generales
    except ZeroDivisionError as e:     
        print('ha ocurrido un error')    
    except ArithmeticError as e:     
        print('ha ocurrido un error')
    except Exception as error:
        print(error)
        
# division_multiple_exception()

def ingreso():
    try:
        a = int(input('Ingrese el valor de a: '))
        b = int(input('Ingrese el valor de b: '))
        print(f'{a} {b}')  
    except ValueError as e:
        ingreso()  # recursividad, se llama a si misma la función.
        
# ingreso()


def ingreso():
    try:
        ingreso_int()
        ingreso_float()
        ingreso_str()
    except ValueError as e:
        print('Error')
        
def ingreso_int():
    a = int(input('Ingrese el valor de a: '))
    b = int(input('Ingrese el valor de b: '))  
    
def ingreso_float():
    a = float(input('Ingrese el valor de a: '))
    b = float(input('Ingrese el valor de b: '))
    
def ingreso_str():
    a = str(input('Ingrese el valor de a: '))
    b = str(input('Ingrese el valor de b: '))
        
            


    
