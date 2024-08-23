def sumar(a, b):
    return a + b

def restar(a: int, b: int):
    return a - b

def multiplar(a , b = 1):
    return a * b

def division(a, b):
    if b == 0:
        # raise ZeroDivisionError('No se puede dividir por cero')
        return 'No se puede dividir por cero'
    else:
        return a / b
    
def ingreso_opcion():
    return input('Ingrese una opcion: \n' 
                 + '1.- sumar\n'
                 + '2.- restar\n' 
                 + '3.- multiplicar\n' 
                 + '4.- dividir\n' 
                 + '5.- salir\n')
    
def ingreso_valores_a_calcular():    
    num_uno = ingreso_numero('ingrese el primero: ')
    num_dos = ingreso_numero('ingrese el segundo: ')       
    return (num_uno, num_dos)

def ingreso_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print('Opción invalida, ingrese un número')
  
    
def verificar_opcion(opcion_ingresada):
     match opcion_ingresada:
         case '1':
            num_uno, num_dos = ingreso_valores_a_calcular()
            return sumar(num_uno, num_dos)
         case '2':
            num_uno, num_dos = ingreso_valores_a_calcular() 
            return restar(num_uno, num_dos)
         case '3':
            num_uno, num_dos = ingreso_valores_a_calcular() 
            return multiplar(num_uno, num_dos)
         case '4':
            num_uno, num_dos = ingreso_valores_a_calcular() 
            return division(num_uno, num_dos)
         case '5':
            return None
         case _:
            return 'Opción invalida'

def verificar_resultado(resultado):
    if resultado == None:
        return False         
    
def calculadora():
    while True:
        opcion_ingresada = ingreso_opcion()
        resultado = verificar_opcion(opcion_ingresada)
        if resultado == None:
            break
        print('El resultado es: ', resultado)

calculadora()
