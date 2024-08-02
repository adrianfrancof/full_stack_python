# las variables de declaran con un nombre, que es su identificador
#van escritas en snake_case
#identificador = valor
nombre_variable = 'una variable'
nombre_variable = 2 #sustituye el valor de la variable

print(nombre_variable) #2

# variables locales y variables globales
s = 'una variable global'

#las variables locales existen dentro de los bloques de codigo
# funciones, condicionales (if, else if), bucles (ciclos)
def f(cualquier_nombre):
    cualquier_nombre = 'sustituimos la variable global'
    variable_local = 'una variable local'
    print(s)
    
f(s) #invocando funcion f
#print(variable_local) #error, variable local no definida
print(s) #una variable global