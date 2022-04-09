'''
4. Leia duas matrizes 3 x 3 e escreva uma terceira com os maiores valores de cada posiçãp
das matrizes lidas.
Entrada:          Saída:
1 2 3             1 3 3
4 5 6             5 5 6
7 8 9             7 9 9

0 3 2
5 4 5
6 9 8
'''
matriz1 = []
matriz2 = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor  [ {i + 1} ] [ {j + 1} ] da matriz 1: "))
        linha.append(valor)
    matriz1.append(linha)

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor  [ {i + 1} ] [ {j + 1} ] da matriz 2: "))
        linha.append(valor)
    matriz2.append(linha)

matriz3 = []
for i in range(3):
    linha = []
    for j in range(3):
        if matriz1[i][j] >= matriz2[i][j]:
            linha.append(matriz1[i][j])
        else:
            linha.append(matriz2[i][j])
    matriz3.append(linha)

# Mostrano as matrizes
for linha in range(3):
    for coluna in range(3):
        print(matriz1[linha][coluna], end=" ")
    print()

print()

for linha in range(3):
    for coluna in range(3):
        print(matriz2[linha][coluna], end=" ")
    print()

print()

for linha in range(3):
    for coluna in range(3):
        print(matriz3[linha][coluna], end=" ")
    print()
