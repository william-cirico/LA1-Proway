'''
1. Leia uma matriz 3 x 3, conte e escreva quantos valores maiores que 10 ela possui.
'''
matriz = []
quantidade_maior_10 = 0
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor  [ {i + 1} ] [ {j + 1} ] da matriz: "))
        linha.append(valor)

        if valor > 10:
            quantidade_maior_10 += 1

    matriz.append(linha)

# Mostrando a matriz
for linha in range(3):
    for coluna in range(3):
        print(matriz[linha][coluna], end=" ")
    print()

print(f"Quantidade de valores maiores que 10: {quantidade_maior_10}")

