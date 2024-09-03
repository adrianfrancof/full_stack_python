class Accesadores:
    def __init__(self):
        self.atributo_publico = 'public' # atributo accedido en toda la estructura
        self._atributo_privado = 'private' # atributo solo accedido en las subclases o por getters y setters
        self.__atributo_protegido = 'protected' # accedido solo en la case que esta declarado
    
    # accesadores y mutadores (getters and setters)    
    def get_variable_privada(self): # acceso a una variable declarada como private
        return self._atributo_privado
    
    def set_variable_privada(self, valor): # asignacion a una variable declarada como private
        self._atributo_privado = valor
        
        
objeto = Accesadores()
print(objeto._Accesadores__atributo_protegido) # acceso a un atributo protegido, mangle named '_Nombre_clase__atributo_protegido'

print(objeto.get_variable_privada()) # acceso a una variable privada

print(objeto.atributo_publico) # acceso a un atributo publico

print(objeto.__atributo_protegido) # AttributeError: 'Accesadores' object has no attribute '__atributo_protegido'. Did you mean: '_atributo_privado'?