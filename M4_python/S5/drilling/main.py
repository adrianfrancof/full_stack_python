from persona import Persona
from trabajador import Trabajador
from departamento import Departamento

if __name__ == "__main__": # punto de inicio de la aplicación
    trabajador  = Trabajador('Juan', 'Perez', 2005, 'Ingenieria Software', 'IS', '200000')

    print(trabajador.__dict__)
    print(f'El objeto es instancia de Persona? {isinstance(trabajador, Persona)}')
    print(f'El objeto es instancia de Trabajador? {isinstance(trabajador, Trabajador)}')
    print(f'El objeto es instancia de Departamento? {isinstance(trabajador, Departamento)}')