import csv

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
        
    def guardar(self,nombre_archivo): 
        archivo = open(nombre_archivo, "a", newline='') 
        datos = [(self.__class__, self.__dict__)] 
        archivo_csv = csv.writer(archivo) 
        archivo_csv.writerow(datos) 
        archivo.close()
    
    def recuperar(nombre_archivo): 
        objetos = [] 
        archivo = open(nombre_archivo, "r") 
        archivo_csv = csv.reader(archivo) 
        for temp in archivo_csv: 
            objetos.append(temp)
        archivo.close() 
        return objetos    
        

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
    
class Particular(Automovil):
    def __init__(self, marca: str, modelo: str, numero_ruedas: int, velocidad: int, cilindrada: int, numero_asientos :int) -> None:
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada)
        self._numero_asientos = numero_asientos    

class Carga(Automovil):
    def __init__(self, marca: str, modelo: str, numero_ruedas: int, velocidad: int, cilindrada: int, carga_maxima :int ) -> None:
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada)
        self._carma_maxima = carga_maxima
        
class Bicicleta(Vehiculo):
    def __init__(self, marca: str, modelo: str, numero_ruedas: int, tipo :str) -> None:
        super().__init__(marca, modelo, numero_ruedas)
        self._tipo = tipo

class Motocicleta(Bicicleta):
    def __init__(self, marca: str, modelo: str, numero_ruedas: int, tipo: str, numero_radios :int, cuadro :str, motor :str) -> None:
        super().__init__(marca, modelo, numero_ruedas, tipo)
        self._numero_radios = numero_radios
        self._cuadro = cuadro
        self._motor = motor


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

# lista = orquestacion_creacion()
# print('Lista de vehiculos: ')
# imprimir_objetos(lista)

particular = Particular("Ford", "Fiesta", 4, "180", "500", 5) 
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000") 
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera") 
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)

print('Motocicleta es instancia con relación a Vehículo:', isinstance(motocicleta, Vehiculo))
print('Motocicleta es instancia con relación a Automovil:', isinstance(motocicleta, Automovil))
print('Motocicleta es instancia con relación a Vehículo particular:', isinstance(motocicleta, Particular))
print('Motocicleta es instancia con relación a Vehículo de Carga:', isinstance(motocicleta, Carga))
print('Motocicleta es instancia con relación a Bicicleta:', isinstance(motocicleta, Bicicleta))
print('Motocicleta es instancia con relación a Motocicleta:', isinstance(motocicleta, Motocicleta))

particular.guardar('vehiculos.csv')
carga.guardar('vehiculos.csv')
bicicleta.guardar('vehiculos.csv')
motocicleta.guardar('vehiculos.csv')        