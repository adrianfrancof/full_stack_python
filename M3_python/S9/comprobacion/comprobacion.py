""" Crear una función que acepte dos parámetros (base y altura) y calcule el área de un rectángulo.
Validar que ambos sean números positivos."""
 
def calcular_area_rectangulo (base, altura):
    if base <= 0 or altura <= 0 :
        return "El numero que ingreso en negativo"
   
    return base * altura
 
 
base = float(input("Ingrese la base \n"))
altura = float(input("Ingrese la altura \n"))
 
print("El area del rectangulo es: ", calcular_area_rectangulo(base,altura))