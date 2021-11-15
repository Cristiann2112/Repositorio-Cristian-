#Imprima solo los valores de esa lista que sean números perfectos e imprima el total de números de perfectos en esa lista.

# 496 -> 1, 2, 4, 8, 16, 31, 62, 124, 248 =>  1 + 2 + 4 + 8 + 16 + 31 + 62 + 124 + 248 = 6
# 28 -> 1, 2, 4, 7, 14 => 1 + 2 + 4 + 7 + 14 = 28

def es_numero_perfecto(numero):
    suma = 0

    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    
    return suma == numero


print ("Indicando que el 28 y 496 son los unicos numeros perfectos. Por ello se indican que son verdaderos  y se repiten un total de 4 veces")
print(es_numero_perfecto(28))
print(es_numero_perfecto(496))
 
