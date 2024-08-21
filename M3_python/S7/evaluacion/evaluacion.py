'''
Dada una lista de diccionarios que representan información de estudiantes, realiza las siguientes tareas:

estudiantes = [ 
    {'nombre': 'Juan', 'edad': 17, 'calificaciones': [85, 90, 88]}, 
    {'nombre': 'María', 'edad': 19, 'calificaciones': [92, 89, 90]}, 
    {'nombre': 'Pedro', 'edad': 21, 'calificaciones': [85, 95, 80]}, 
    {'nombre': 'Ana', 'edad': 18, 'calificaciones': [90, 92, 87]}, 
    {'nombre': 'Luis', 'edad': 20, 'calificaciones': [88, 85, 92]}, 
]

Se debe imprimir cada dato de las listas en pantalla con las siguientes excepciones:
• Filtra y muestra únicamente los estudiantes que tienen más de 18 años y cuyo promedio de calificaciones sea superior a 85.
• Calcula el promedio de las calificaciones de los estudiantes que tienen más de 18 años y cuya edad sea un número primo.
'''

def es_primo(numero):
    if numero < 2:
        return False
    for i in range (2, numero): # int(numero**0.5) + 1
        if numero % i  == 0:
            return False
    return True

def promedio_notas(lista):
    return sum(lista) / len(lista)

estudiantes = [ 
    {'nombre': 'Juan', 'edad': 17, 'calificaciones': [85, 90, 88]}, 
    {'nombre': 'María', 'edad': 19, 'calificaciones': [92, 89, 90]}, 
    {'nombre': 'Pedro', 'edad': 21, 'calificaciones': [85, 95, 80]}, 
    {'nombre': 'Ana', 'edad': 18, 'calificaciones': [90, 92, 87]}, 
    {'nombre': 'Luis', 'edad': 20, 'calificaciones': [88, 85, 92]}, 
]

# Filtra y muestra únicamente los estudiantes que tienen más de 18 años y cuyo promedio de calificaciones sea superior a 85.
estudiantes_filtrados = []
for estudiante in estudiantes:
    if estudiante['edad'] > 18 and promedio_notas(estudiante['calificaciones']) > 85:
        # filtrar el estudiante
        estudiantes_filtrados.append(estudiante)
        if es_primo(estudiante['edad']):
            print(f'{estudiante['nombre']}:')
            print(f'Promedio calificacion {promedio_notas(estudiante['calificaciones'])} \n')
            
    
# Calcula el promedio de las calificaciones de los estudiantes que tienen más de 18 años y cuya edad sea un número primo.
# for estudiante in estudiantes_filtrados: 
#     if es_primo(estudiante['edad']):
#         print(f'{estudiante['nombre']}:')
#         print(f'Promedio calificacion {promedio_notas(estudiante['calificaciones'])} \n')
