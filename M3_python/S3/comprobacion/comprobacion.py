# Requerimos imprimir en pantalla el resultado de la multiplicación de
# dos variables, las cuales llamaremos “a y b”, 
# y les asignaremos los valores 20 y 30, respectivamente. 
# Debemos documentar cada paso de la operación haciendo uso de comentarios.

# declarar variables
a = 20
b = 30

# operacion a realizar
c = a * b

# imprimir resultado
print(c)
print("El resultado de la multiplicacion es: ", c)
print(f'El resultado de la multiplicacion es: {c}')
print(f'El resultado de multiplicar {a} y {b} es: {c}')
print('El resultado de multiplicar {} y {} es: {}'.format(a, b, c))
print('El resultado de la multiplicacion es: ' + c) # TypeError: can only concatenate str (not "int") to str
print('El resultado de la multiplicacion es: ' + str (c))