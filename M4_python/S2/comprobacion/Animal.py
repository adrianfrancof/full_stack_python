class Animal:
    def __init__(self, nombre, edad, raza, peso):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.peso = peso
        
    def __str__(self) -> str:
        f'Animal(nombre:{self.nombre})'
        
# identificador =  Object(atributos, atributos)       
caballo = Animal('Rayo', 2, 'pura sangre', 600)                   
leon    = Animal('Leoncin', 3, 'Leon', 450)