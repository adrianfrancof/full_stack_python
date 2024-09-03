class Vehiculo:
    def __init__(self, marca,motor):
        self.marca = marca
        self.motor = motor  # atributo tipo objeto es necesario para crear el objeto Vehiculo
        
class Motor:
    def __init__(self, cilindraje,tipo):
        self.cilindraje = cilindraje
        self.tipo = tipo

motor = Motor(4,'bencina')        
vehiculo = Vehiculo('Chevrolet', motor)       