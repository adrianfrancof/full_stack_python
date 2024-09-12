class Persona:
    def __init__(self, nombre, apellido, rut):
        self._nombre   = nombre   # atributos privados _nombre_variable
        self._apellido = apellido
        self._rut      = rut
        
    # accesadores y mutadores (getters y setters)
    @property        # get
    def nombre(self):             # def get_nombre()
        return self._nombre
    
    @nombre.setter   # set
    def nombre(self, nombre):     # def set_nombre(self, nombre):
        self._nombre = nombre
    
    @property        # get    
    def apellido(self):            # def get_apellido()
        return self._apellido
    
    @apellido.setter # set
    def apellido(self, apellido):  # def set_apellido(self, apellido):
        self._apellido = apellido
        
    @property        # get
    def rut(self):                 # def get_rut()
        return self._rut
    
    @rut.setter       # set
    def rut(self, rut):             # def set_rut(self, rut):
        self._rut = rut
        
    def get_tipo(self):
        print(f'Soy del tipo \n{self}')
        print(type(self))
        
    def __str__(self) -> str:
        return f'Persona(nombre:{self._nombre}, apellido:{self._apellido}, rut:{self._rut})'