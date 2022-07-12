"""
10) Faça um programa que leia 10 números e preencha um vetor, calcule e
mostre a quantidade de numeros negativos e a soma dos números positivos desse vetor.
"""

numeros = []
negativos = []
positivos = []

for i in range(10):
    numero = int(input("Digite um numero: "))
    numeros.append(numero)
    if numero >= 0:
        positivos.append(numero)
    else:
        negativos.append(numero)


soma_positivos = sum(positivos)
quan_negativos = len(negativos)

print(f"""

Os numeros digitados foram: {numeros}
A quantidade de negativos é: {quan_negativos}
A soma dos positivos é: {soma_positivos}

""")


