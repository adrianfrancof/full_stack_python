from persona import Persona
from departamento import Departamento

class Trabajador(Persona, Departamento):
    
    def __init__(self, nombre, apellido, annio, nombre_dpto, nombre_corto_dpto, salario):
        super().__init__(nombre, apellido, annio)
        Departamento.__init__(self, nombre_dpto, nombre_corto_dpto)
        self.salario = salario