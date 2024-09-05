from model.Persona import Persona

class Supervisor(Persona):
    def __init__(self, nombre, apellido, rut, area):
        super().__init__(nombre, apellido, rut)
        self._area = area
        
    # accesadores y mutadores (getters y setters)
    @property             # get
    def area(self):
        return self._area
    
    @area.setter          # set
    def area(self, area):
        self._area = area