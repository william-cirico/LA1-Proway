import math


numero = int(input("Digite um número"))

if numero > 0:
    raiz = math.sqrt(numero)
    print(f"Raiz quadrada de {numero}: {raiz}")
else:
    quadrado = numero ** 2
    print(f"Número ao quadrado: {quadrado}")