# diccionarios en python
# estructura para almacenar datos en pares clave-valor
# no tienen un orden específico
# colección de datos no ordenados
# se declaran con {}

# estudiantes {'Fulanito': 20, 'Maria': 22, 'Jose': 40, 'Marta': 50}
estudiantes = {
    #clave : valor
    'Fulanito': 20,
    'Maria': 22,
    'Jose': 40,
    'Marta': 50
}

#acceder a un valor del diccionario, es atraves de su clave o key
# nombre_diccionario['clave']
print(estudiantes['Fulanito']) #20

# get(clave) retorna el valor de la clave
estudiantes.get('Fulanito') #20

valor_retornado = estudiantes.pop('Fulanito') #elimina la clave 'Fulanito' del diccionario

claves = estudiantes.keys() #retorna las claves del diccionario
print(claves) #dict_keys(['Maria', 'Jose', 'Marta'])

valores = estudiantes.values() #retorna los valores del diccionario
print(valores) #dict_values([22, 40, 50])