# estructuras condicionales, pueden controlar el flujo del aplicativo
# if, elif, else

print('Ingrese un número:')
num = input() #input() siempre retorna un string
num = int(num) #convertir el string a entero

if(num > 0):
    print('El número es positivo')
elif(num < 0):
    print('El número es negativo')
else:
    print('El número es cero')
    
#------------------------------------------------
if num > 0:
    print('El número es positivo')
elif num < 0:
    print('El número es negativo')
else:
    print('El número es cero')       