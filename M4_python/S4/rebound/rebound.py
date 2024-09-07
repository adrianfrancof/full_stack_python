class Libro:
    
    def __init__(self, autor=None, titulo=None, anio_publicacion=None):
        self._autor =  autor
        self._titulo = titulo
        self._anio_publicacion = anio_publicacion
        
    @property
    def autor(self):
        return self._autor
    
    @autor.setter
    def autor(self, autor):
        self._autor = autor
        
    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo
    
    @property
    def anio_publicacion(self):
        return self._anio_publicacion
    
    @anio_publicacion.setter
    def anio_publicacion(self, anio_publicacion):
        self._anio_publicacion = anio_publicacion        
        
              
libro_1 = Libro()
libro_1.autor = 'Dan Brown'
libro_1.titulo = 'Infierno'

libro_2 = Libro()
libro_2.autor = 'Dan Brown'
libro_2.titulo = 'El Código Davinci'
libro_2.anio_publicacion = 2003

print(libro_1.__dict__)
print(libro_1.__str__)

print(libro_2.__dict__)
print(libro_2.__str__)