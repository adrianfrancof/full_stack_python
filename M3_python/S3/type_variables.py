# comenzamos con los tipos de variables en python

"""
Bloque de comentario
se puede escribir comentarios de una linea o agregar un bloque de comentario
se necesita 3 comillas dobles para abrir y cerrar el bloque de comentario
"""

'''
Comillas sencillas tambien se pueden usar para abrir y cerrar un bloque de comentario
'''

#método de impresión en consola
print("Full stack python") #imprime un mensaje en consola
print(2) #imprime un número entero
print(2+1)
#print(2+'1') #SyntaxError: unterminated string literal

#declaracion de variables
# las variables el nombre de la variable es su identificador
cadena = 'Hola mundo' #variable de tipo string, una cadena de caracteres

#indentacion en python, se realiza con tabulaciones o espacios
# if (true) {
#   print('True')
#   print('Otra impresion')
#   if (true) {
#   print('indentacion en python')
#   }    
# }    
if True:
    print('True')
    print('Otra impresion')
    if True:
        print('indentacion en python')


#otro bloque de código                       
if True:
    print('False')
    
    
print('separación de código se realiza con dos saltos de linea')

#tipos de datos en python
# funcion type(variable) para saber el tipo de dato de una variable
print(type(cadena)) #<class 'str'>
print(type(2)) #<class 'int'>
print(type(2.0)) #<class 'float'>
print(type(True)) #<class 'bool'>
print(type(False)) #<class 'bool'>
print(type(None)) #<class 'NoneType'>
print(type(2+1j)) #<class 'complex'>
print(type(1j)) #<class 'complex'>
print(type([])) #<class 'list'>