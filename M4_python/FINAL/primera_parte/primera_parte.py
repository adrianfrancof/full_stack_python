class Vehiculo:
    def __init__(self, marca :str, modelo :str, numero_ruedas :int) -> None:
        self._marca = marca
        self._modelo = modelo
        self._numero_ruedas = numero_ruedas
        
    @property
    def marca(self) -> str:
        return self._marca
    
    @marca.setter
    def marca(self, marca :str) -> None:
        self._marca = marca
        
    @property
    def modelo(self) -> str:
        return self._modelo
    
    @modelo.setter
    def modelo(self, modelo :str) -> None:
        self._modelo = modelo
        
    @property
    def numero_ruedas(self) -> int:
        return self._numero_ruedas
    
    @numero_ruedas.setter
    def numero_ruedas(self, numero_ruedas :int) -> None:
        self._numero_ruedas = numero_ruedas
        

class Automovil(Vehiculo):
    def __init__(self, marca: str, modelo: str, numero_ruedas: int, velocidad :int, cilindrada :int) -> None:
        super().__init__(marca, modelo, numero_ruedas)
        self._velocidad = velocidad
        self._cilindrada = cilindrada
    
    @property
    def velocidad(self) -> int:
        return self._velocidad
    
    @velocidad.setter
    def velocidad(self, velocidad :int) -> None:
        self._velocidad = velocidad
        
    @property
    def cilindrada(self) -> int:
        return self._cilindrada
    
    @cilindrada.setter
    def cilindrada(self, cilindrada  :int) -> None:
        self._cilindrada = cilindrada
        
    def __str__(self) -> str:
        return f'Datos del automóvil: Marca {self._marca}, Modelo {self._modelo}, {self._numero_ruedas} ruedas {self._velocidad} Km/h, {self._cilindrada} cc'    

def crear_vehiculo() -> Automovil:
    marca = input('Inserte la marca: ')
    modelo = input('Inserte el modelo: ')
    numero_ruedas = input('Inserte el número de ruedas: ')
    velocidad = input('Inserte la velocidad km/h: ')
    cilindrada = input('Inserte la cilindrada en cc: ')
    return Automovil(marca, modelo, numero_ruedas, velocidad, cilindrada)

def imprimir_objetos(lista):
    for i in lista:
        print(i)

def ingreso_cantidad() -> int:
    return int(input('Cuantos vehiculos desea insertar: '))

def orquestacion_creacion() -> list[Automovil]:
    cantidad_ingresos = ingreso_cantidad()
    
    lista_vehiculos = []
    for i in range(0, cantidad_ingresos):
        print('Datos del automovil ', i+1)
        vehiculo = crear_vehiculo()
        lista_vehiculos.append(vehiculo)
        
    return lista_vehiculos

lista = orquestacion_creacion()
print('Lista de vehiculos: ')
imprimir_objetos(lista)
        