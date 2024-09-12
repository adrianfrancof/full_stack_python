from model.Cliente import Cliente
from model.Supervisor import Supervisor
from service.ClienteService import ClienteService
from service.SupervisorService import SupervisorService
from service.MenuService import MenuService

# instancias globales
# menu_service = MenuService()
# cliente_service = ClienteService()
# supervisor_service = SupervisorService()

def main():
    # creacion de instancias para acceso a los servicios, instancias locales
    menu_service = MenuService()
    cliente_service = ClienteService()
    supervisor_service = SupervisorService()
    
    while True:
        menu_service.imprimir_menu()
        opcion = input('Ingrese una opción:')
        
        if opcion == '1':
            cliente_service.crear_cliente()
        elif opcion == '2':
            supervisor_service.crear_supervisor()
        elif opcion == '3':
            print('Saliendo...')
            break
        else:
            print('Opcion invalida')            
    pass

# punto de entrada o ejecucion del programa
if __name__ == '__main__':
    main()