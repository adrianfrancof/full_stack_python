class Persona:
    def __init__(self, id, nombre, apellidos, edad):
        self.id        = id
        self.nombre    = nombre
        self.apellidos = apellidos
        self.edad      = edad
        
class Cuenta:
    def __init__(self, id, saldo, id_persona):
        self.id = id
        self.saldo = saldo
        self.id_persona = id_persona
        
        
persona = Persona(1,'Fulanito','Perez', 35)
cuenta  = Cuenta(1000,0,1)        