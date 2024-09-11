'''
Custom exception, son exceptiones creadas por el desarrollador y que simplemente heredan de la clase base Exception
'''
import json

class CustomException(Exception):
    # constructor
    def __init__(self, mensaje, codigo) -> None:
        super().__init__(mensaje)
        self.codigo = codigo
        
        
def excepcion_propia():
    try:
        edad = int(input("Ingrese su edad: "))
        if edad < 0:
            raise CustomException("Ha sucedido un error de negocio", 460) # ejecutar una excepcion personalizada
        print(json.dumps({'edad': edad}))
    except ValueError as e:
        # print("Error, ingrese un numero")
        print(json.dumps({'mensaje': 'Error: ingrese un numero'}))
    except CustomException as e:
        # print(f'Mensaje: {e}')
        # print(f'Codigo: {e.codigo}')
        response = {
            'mensaje': str(e),
            'codigo' : e.codigo
        }
        print(json.dumps(response))
     
excepcion_propia()

# {
#     'mensaje': 'Ha sucedido un error de negocio',
#     'codigo' : 460
# }