'''
Los objetos comienzan con la palabra class, inician con el nombre del objeto en mayuscula
Los objetos tienen constructor(crear la instancia) y accesadores.
'''
#class nombre_objeto:
class Vehiculo:
    # constructor con parametros, se necesitan todos los atributos o parametros para instanciar al objeto
    def __init__(self, marca, color, modelo, peso, ancho, alto):
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.peso = peso
        self.ancho = ancho
        self.alto = alto
    
    # constructor vacio o construcor sin parametros, se pueden omitir los atributos
    def __init__(self, marca=None, color=None, modelo=None, peso=None, ancho=None, alto=None):
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.peso = peso
        self.ancho = ancho
        self.alto = alto
        
    def arrancar(self):
        print(f'El vehiculo {self.marca} {self.modelo} arranco')
        
    def frenar(self):
        print(f'El vehiculo {self.marca} {self.modelo} frena')
    
    def girar_izquierda(self):
        print(f'El vehiculo {self.marca} {self.modelo} gira a la izquierda')
        
    def girar_derecha(self):
        print(f'El vehiculo {self.marca} {self.modelo} gira a la derecha')
        
    def apagar(self):
        print(f'El vehiculo {self.marca} {self.modelo} apaga')
        
    def encender(self):
        print(f'El vehiculo {self.marca} {self.modelo} encendido')
        
    def retroceder(self):
        print(f'El vehiculo {self.marca} {self.modelo} retrocede', end='\n')
    
    # funcion para imprimir los objetos en String y no la referencia en memoria del objeto    
    def __str__(self) -> str:
        return f'Vehiculo [marca:{self.marca}, color:{self.color}, modelo:{self.modelo}, peso:{self.peso}, ancho:{self.ancho}, alto:{self.alto}]'    


# instancia de Vehiculo invocando al constructor con parametros        
vehiculo = Vehiculo('BMW', 'Blanco', 'M3', '1500', '2', '1.5')
vehiculo.color = 'Rojo'

# instancia de Vehiculo sin parametros, se omiten los atributos
vehiculo_uno = Vehiculo()
vehiculo_uno.marca = 'Chevrolet' # asignando los atributos del objeto
vehiculo_uno.color = 'Negro'     # asignando los atributos del objeto
vehiculo_uno.modelo = 'Aveo'     # asignando los atributos del objeto
vehiculo_uno.peso = '1500'       # asignando los atributos del objeto
vehiculo_uno.ancho = '2'         # asignando los atributos del objeto

# instancia de Vehiculo invocando al constructor con parametros
# class Vehiculo(
#     marca: Any  | None = None,
#     color: Any  | None = None,
#     modelo: Any | None = None,
#     peso: Any   | None = None,
#     ancho: Any  | None = None,
#     alto: Any   | None = None
# )     
vehiculo_dos = Vehiculo('Ford', 'Amarillo', 'Fiesta', 1000, 1.5, 1.5)

# instancia de Vehiculo sin parametros, se omiten los atributos
vehiculo_tres = Vehiculo()
vehiculo_tres.marca  = 'Chery' # asignando los atributos del objeto


# invocando metodos del objeto, accediendo a los métodos del objeto
vehiculo.encender()
vehiculo.arrancar()
vehiculo.girar_izquierda()
vehiculo.girar_derecha()
vehiculo.retroceder()
print('---------------------------------------------')
vehiculo_uno.encender()

# impresión del objeto, usara la funcion def __str__ definida dentro del objeto
print(vehiculo)
print(vehiculo_uno)

            