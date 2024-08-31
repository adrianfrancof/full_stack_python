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
        
    #accesadores o mutadores, se usan para modificar los atributos del objeto
    def get_marca(self):        # vehiculo.get_marca()
        return self.marca
    
    def set_marca(self, marca):   # vehiculo.set_marca('Toyota')
        self.marca = marca
        
    def get_color(self):          # vehiculo.get_color()
        return self.color
    
    def set_color(self, color):   # vehiculo.set_color('Rojo')
        self.color = color
        
    def get_modelo(self):         # vehiculo.get_modelo()
        return self.modelo
    
    def set_modelo(self, modelo): # vehiculo.set_modelo('Corolla')
        self.modelo = modelo
        
    def get_peso(self):           # vehiculo.get_peso()
        return self.peso
    
    def set_peso(self, peso):     # vehiculo.set_peso('1500')
        self.peso = peso
        
    def get_ancho(self):          # vehiculo.get_ancho()
        return self.ancho
    
    def set_ancho(self, ancho):   # vehiculo.set_ancho('1500')
        self.ancho = ancho
        
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
vehiculo.color = 'Rojo' # set asignando valor a un atributo
print(vehiculo.color)   # get accediendo imprimiendo el valor del atributo
print(id(vehiculo))     # id devuelve la referencia en memoria del objeto


# accediendo a los atributos con metodos accesadores (get) y mutadores (set)
vehiculo.set_color('Azul')     # set asignando valor a un atributo
print(vehiculo.get_color())    # get accediendo imprimiendo el valor del atributo


# instancia de Vehiculo sin parametros, se omiten los atributos
vehiculo_uno = Vehiculo()
vehiculo_uno.marca = 'Chevrolet' # asignando los atributos del objeto
vehiculo_uno.color = 'Negro'     # asignando los atributos del objeto
vehiculo_uno.modelo = 'Aveo'     # asignando los atributos del objeto
vehiculo_uno.peso = '1500'       # asignando los atributos del objeto
vehiculo_uno.ancho = '2'         # asignando los atributos del objeto
print(id(vehiculo_uno))

# accediendo a los atributos con metodos accesadores (get) y mutadores (set)
vehiculo_uno.set_marca('Chevrolet')      # set asignando valor a un atributo
vehiculo_uno.set_color('Negro')          # set asignando valor a un atributo
vehiculo_uno.set_modelo('Aveo')          # set asignando valor a un atributo

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

            