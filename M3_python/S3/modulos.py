# los modulos son importados al proyecto como librerias que realizan alguna función
#ejemplo el modulo math, para realizar operaciones matematicas
# las librerias o modulos se importan al comienzo del archivo
from math import pi as PI_VALUE #importar una función específica de un modulo
import math            #importar todo el modulo
from math import *     #importar todo el modulo

#para acceder a las funciones de un modulo se utiliza la notación de punto
print(math.sqrt(4)) #2.0
print(math.pi) #3.141592653589793
print(PI_VALUE) #3.141592653589793
print(math.pow(2,3)) #8.0