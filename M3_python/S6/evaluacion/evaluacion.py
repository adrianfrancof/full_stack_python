'''
Se requiere contar con un programa que, dados 3 números diferentes, los evalúe y entregue el orden de mayor a menor.
'''

# ingreso de 3 numeros
num_1 = int(input("Ingrese el primer numero: "))
num_2 = int(input("Ingrese el segundo numero: "))
num_3 = int(input("Ingrese el tercer numero: "))

# comparacion de numeros
if len(set({num_1, num_2, num_3})) != 3:
    print('debe ingresar numeros diferentes')
else :
    ordenados = sorted([num_3, num_2, num_1], reverse = True)
    print(ordenados)