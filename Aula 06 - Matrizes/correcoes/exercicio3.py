'''
3. Leia uma matriz 3 x 3. Leia tambem um valor X. O programa devera fazer uma busca
desse valor na matriz e, ao final, escrever a localização (linha e coluna) ou uma mensa-
gem de “não encontrado”.
'''
from threading import local


matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor  [ {i + 1} ] [ {j + 1} ] da matriz: "))
        linha.append(valor)
    matriz.append(linha)

valor_x = int(input(f"Digite o valor de X: "))

localizacao = ""
for i, linha in enumerate(matriz):
    for j, valor in enumerate(linha):
        if valor_x == valor:
            localizacao = f"[{i}][{j}]"

if localizacao:
    print(localizacao)
else:
    print("Não encontrado.")
