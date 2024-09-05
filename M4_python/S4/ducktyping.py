'''
Ducktyping
Los objetos serán tratados como simples objetos y no por su tipo

Lo que diferencia un objeto de otro es sus atributos y funciones
 
'''

class Perro:
    def hablar(self):
        print('guau')
        
    def sentarse(self):
        print('sentado')    
    
class Gato:
    def hablar(self):
        print('miau')
      
class Pato:
    def hablar(self):
        print('cuac')
        
def llamar_hablar(objeto):
    objeto.hablar()
    
def recorrer_lista_objetos(lista):
    for objeto in lista:
        objeto.hablar()
        if isinstance(objeto, Perro): # verficar si el objeto es un perro, verificación de tipo
            objeto.sentarse()

perro = Perro()
gato = Gato()
pato = Pato()
    
llamar_hablar(perro)
llamar_hablar(gato)
llamar_hablar(pato)

recorrer_lista_objetos([perro, gato, pato])

