#  Defina una función en python que acepte el radio y devuelva el valor del area de un círculo de esas dimensiones.

from math import pi
radio = float(input("Ingrese el radio del círculo:\n"))

area = round((pi * radio ** 2), 3)

print(f"El área del círculo es: {area}")  

