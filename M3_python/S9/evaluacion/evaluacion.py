'''
Crear una función que sume dos números, otra que reste dos números, otra que multiplique dos
números, y otra que divida dos números. Adicionalmente, crear una función que acepte dos
números como parámetros y regrese el resultado en forma de tupla de su suma, resta,
multiplicación y división.
Los resultados se deben almacenar en un diccionario, cuyas claves serán: Suma, Resta,
Multiplicación y División, y los valores de cada clave serán los resultados obtenidos con la función
creada anteriormente.
'''

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b


def resultado(a, b):
           #tupla(1,2,3)
           #tuple(funcion(a,b), funcion(a,b), funcion(a,b))
    return tuple((suma(a, b), resta(a, b), multiplicar(a, b), dividir(a, b)))

def resultado_como_diccionario(a, b):
    return {'suma': suma(a, b), 'resta': resta(a, b), 'multiplicacion': multiplicar(a, b), 'division': dividir(a, b)}

def resultado_como_lista(a, b):
    return list((suma(a, b), resta(a, b), multiplicar(a, b), dividir(a, b)))


def construir_diccionario(resultado):
#clave : valor
    diccionario_resultados = {
        'suma': resultado[0],
        'resta': resultado[1],
        'multiplicacion': resultado[2],
        'division': resultado[3]
        
    }
    return diccionario_resultados

print(construir_diccionario(resultado(20, 15)))
print(construir_diccionario(resultado_como_lista(20, 15)))
print(resultado_como_diccionario(20, 15))