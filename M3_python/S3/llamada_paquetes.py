#import nombre_carpeta.nombre_archivo as alias
import paquete.funciones as f
import paquete.funciones # importar el paquete o modulo sin alias
import paquete.funciones as funciones # importar el paquete o modulo con alias

suma = f.suma(2,3) #5
print(suma)

print(f.resta(2,3)) #-1

paquete.funciones.resta(2,3) #-1

#se necesita definir el alias funciones para que no de error no definido
funciones.restas(2,3) #NameError: name 'funciones' is not defined