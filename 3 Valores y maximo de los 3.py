# Defina una función en python que acepte 3 valores y devuelva solo el maximo de los tres.

def maximo(valores):
    mayor = valores[0]

    for i in range(1, len(valores)):
        if valores[i] > mayor:
            mayor = valores[i]
    
    return mayor


numeros = [1, 2, 3]

print(maximo(numeros))
