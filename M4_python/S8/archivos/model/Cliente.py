from model.Persona import Persona

class Cliente(Persona):
    def __init__(self, nombre, apellido, rut, descuento):
        super().__init__(nombre, apellido, rut)
        self._descuento = descuento
        
    # accesadores y mutadores (getters y setters)
    @property                   # get
    def descuento(self):        
        return self._descuento
    
    @descuento.setter           # set
    def descuento(self, descuento):
        self._descuento = descuento
        
    def __str__(self) -> str:
        return f'Cliente(nombre={self._nombre}, apellido={self._apellido}, rut={self._rut}, descuento={self._descuento})\n'