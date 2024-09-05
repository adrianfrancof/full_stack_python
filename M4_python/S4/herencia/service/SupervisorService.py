from model.Supervisor import Supervisor

class SupervisorService:
    def crear_supervisor(self):
        nombre    = input('Ingrese el nombre del supervisor')
        apellido  = input('Ingrese el apellido del supervisor')
        rut       = input('Ingrese el rut del supervisor')
        area      = input('Ingrese el área del supervisor')
        
        supervisor = Supervisor(nombre, apellido, rut, area)
        print(supervisor)