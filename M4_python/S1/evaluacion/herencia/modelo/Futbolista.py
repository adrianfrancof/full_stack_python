from modelo.Persona import Persona

class Futbolista(Persona):
    def __init__(self, id, nombre, apellidos, edad, dorsal, demarcacion):
        super().__init__(id, nombre, apellidos, edad) # constructor de la clase padre
        
        # Atributos propios de la clase futbolista
        self.dorsal      = dorsal
        self.demarcacion = demarcacion
        
    # métodos heredados
    def concentarse(self):
        super().concentrarse()
        
    def viajar(self):
        super().viajar()
        
    # métodos propios de la clase futbolista
    def jugar_partido(self):
        print("El futbolista {} con dorsal {} está jugando un partido".format(self.nombre, self.dorsal))
        
    def entrenar(self):
        print("El futbolista {} está entrenando".format(self.nombre))