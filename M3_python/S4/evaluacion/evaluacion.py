# diccionarios
# clave: valor

persona_uno = {'nombre': 'Juan', 'apellido': 'Perez', 'telefono': 1234567890}

persona_dos = {
    'nombre': 'Fulanito', 
    'apellido': 'Gonzalez', 
    'telefono': 1234567890
    }

persona_tres = {'nombre': 'Maria', 'apellido': 'Andrade', 'telefono': 1234567890}

lista_personas = [persona_uno, persona_dos, persona_tres]
print(lista_personas)
lista_personas[0]['nombre'] = 'Juanito' # Modificar un valor



# diccionario de diccionarios
personas = {
    'persona_uno' : {'nombre': 'Juan', 'apellido': 'Perez', 'telefono': 1234567890},
    'persona_dos' : {
    'nombre': 'Fulanito', 
    'apellido': 'Gonzalez', 
    'telefono': 1234567890
    },
    'persona_tres' : {'nombre': 'Maria', 'apellido': 'Andrade', 'telefono': 1234567890},
    'persona_cuatro' : {
        'nombre': 'Maria', 
        'apellido': 'Andrade', 
        'telefono': 1234567890,
        'direccion': {
            'calle': 'calle 1',
            'numero': 123,
            'region': 'Metropolitana'
        }
    }
}

#diccionario[clave][subclave]
print(personas['persona_uno']['nombre'])
print(personas['persona_cuatro']['direccion']['region'])
