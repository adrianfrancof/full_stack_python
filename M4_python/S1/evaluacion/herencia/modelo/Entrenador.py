from modelo.Persona import Persona

class Entrenador(Persona):
    def __init__(self, id, nombre, apellidos, edad, id_federecion):
        super().__init__(id, nombre, apellidos, edad) # constructor de super clase
        
        # atributos propios de la clase Entrenador
        self.id_federacion = id_federecion
    
    # Métodos heredados    
    def concentrarse(self):
        Persona.concentrarse() # acceso estatico a traves del nombre de la clase
        
    def viajar(self):
        super().viajar()
        
    # métodos propios de la clase Entrenador
    def dirigir_partido(self):
        print("El entrenador dirige el partido")
        
    def dirigir_entrenamiento(self):
        print("El entrenador dirige el entrenamiento")
        