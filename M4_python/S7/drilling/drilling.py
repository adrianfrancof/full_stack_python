'''
Diseñe una nueva clase de excepción definida por el usuario, que gestione la entrada del valor de una variable salario, y la misma se encuentre entre los valores de 1000 y 2000; de lo contrario, se lanza una excepción que refleja que el salario no se encuentra en el rango de 1000 y 2000.

Ejemplo de la salida del programa: 
Ingrese el salario: 5000 
Traceback (most recent call last): File "drilling-CUE07.py", line 20, in <module> raise RangoSalarioError(salario) __main__.RangoSalarioError: 5000 -> Salario no está definido en el rango (1000 a 2000)
'''

class RangoSalarioError(Exception):
    def __init__(self, mensaje, salario) -> None:
        super().__init__(mensaje)
        self.salario = salario
        self.mensaje = mensaje
        
    def __str__(self) -> str:
        return f' {self.salario} -> {self.mensaje}'
    
def validar_salario():
    try:
        salario = int(input('Ingrese el salario: '))
        if not (1000 <= salario <= 2000):
            raise RangoSalarioError('Salario no está definido en el rango (1000 a 2000)', 5000)
        print(f'El salario {salario} se encuentra dentro del rango')
    except Exception as e:
        print('Error:', str(e))

validar_salario()