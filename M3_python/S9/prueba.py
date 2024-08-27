c = 'hola un mensaje' # variable global


def imprimir_mensaje():
    c = 'cambio de valor' # llamada avariable global
    print(c)
    
def imprimir_mensaje(c):
    c = 'cambio de valor' # llamada a variable local compartida como parametro de entrada
    print(c)
    
def imprimir_mensaje(c, e): 
    c = 'cambio de valor' # llamada a variable local compartida como parametro de entrada
    print(c)  
    
def imprimir_mensaje_otra(c):
    a = c                 # llamada a variable local compartida como parametro de entrada
    print(a)        
    
imprimir_mensaje()

