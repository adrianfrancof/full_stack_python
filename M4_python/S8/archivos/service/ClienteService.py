from model.Cliente import Cliente

class ClienteService:
    
    def __init__(self):
        self._clientes = self.load_clientes()
        
    def load_clientes(self):
        try:
            with open('clientes.txt', 'r') as file:
                clientes = file.readlines()
        except FileNotFoundError:
            clientes = []
            with open('clientes.txt', 'w') as file:
                file.writelines(clientes)
        return clientes
    
    def save_clientes(self):
        with open('clientes.txt', 'w') as file:
            for i in self._clientes:
                file.write(str(i))              
    
    def crear_cliente(self):
        nombre    = input('Ingrese el nombre del cliente: ')
        apellido  = input('Ingrese el apellido del cliente: ')
        rut       = input('Ingrese el rut del cliente: ')
        descuento = input('Ingrese el descuento del cliente: ')
        
        cliente = Cliente(nombre, apellido, rut, descuento)
        print(cliente)
        
        #se añade el nuevo cliente a la lista de clientes
        self._clientes.append(cliente)
        # guarda los cambios en el archivo
        self.save_clientes()
          
        