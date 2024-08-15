'''
Diccionario de Estudiantes y Notas
Enunciado: Escribe un programa que pida al usuario los nombres y las notas de varios estudiantes, y luego almacene esta información en un diccionario. Después, el programa debe permitir al usuario consultar la nota de un estudiante ingresando su nombre.
'''
estudiantes = {} # diccionario para toda la ejecucion

# {   "key": "value"
#     "nombre": "nota",
#     "nombre": "nota",
# }

def ingreso_datos():
    nombre_estudiante = input('Ingrese el nombre del estudiante:')
    nota_estudiante = int(input('Ingrese la nota del estudiante:'))
    return [nombre_estudiante, nota_estudiante]

def agregar_estudiante(nombre_estudiante, nota_estudiante):
    # diccionario[key] = value
    estudiantes[nombre_estudiante] = nota_estudiante
    
def consultar_estudiante(nombre_estudiante):
           # diccionario.get(key, default)
           # diccionario[key]
    return estudiantes.get(nombre_estudiante, 'No se encontro el estudiante')

def ingreso_opcion_menu():
    return input('Bienvenido, que desea realizar:\n'
                            +'1.- agregar estudiante\n'
                            +'2.- consultar estudiante\n'
                            +'3.- salir\n'
                            +'Ingrese una opcion:')

def validacion(opcion_ingresada):
     match opcion_ingresada:
            case '1':
                # Agregar Estudiantes
                lista = ingreso_datos()
                agregar_estudiante(lista[0], lista[1])
            case '2':
                # Consultar estudiante    
                nombre_estudiante = input('Ingrese el nombre del estudiante a consultar la nota:')
                nota_encontrada = consultar_estudiante(nombre_estudiante)
                print(f'La nota del estudiante encontrado es {nota_encontrada}\n')
            case '3':
                print('Hasta luego...')
            case _ :
                print('ópcion invalida\n')
            

def menu():      
    while True:
        opcion_ingresada = ingreso_opcion_menu()
        validacion(opcion_ingresada)
        
           
menu() # inicio del programa                
            