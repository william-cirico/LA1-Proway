"""
1) Leia um vetor de 10 posições. Calcule e escreva quantos valores 
pares ele possui.
"""
from random import randint


pares = []
# for i in range(3):
#     valor = int(input(f"Digite o {i + 1}º valor: "))

#     if valor % 2 == 0:
#         pares.append(valor)

# print(f"Foram digitados: {len(pares)} valor(es) par(es)")

for i in range(1000):
    valor = randint(1, 100)

    if valor % 2 == 0:
        pares.append(valor)

print(pares)
print(f"Foram digitados: {len(pares)} valor(es) par(es)")


