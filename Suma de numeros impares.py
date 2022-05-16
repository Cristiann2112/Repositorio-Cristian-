#  Dado una lista de enteros, defina una función en python que devuelva la suma de solo los valores impares de dicha lista.:
#Tomando una lista predeterminada desde el 1 al 10.
numeros = [1, 2, 3, 4, 5 ,6 ,7 ,8 ,9 ,10]
suma_impares = 0

for i in range(len(numeros)):
    if numeros[i] % 2 == 1:
        suma_impares += numeros[i]

print('La suma de los números impares que hay en la lista es igual a', suma_impares)
