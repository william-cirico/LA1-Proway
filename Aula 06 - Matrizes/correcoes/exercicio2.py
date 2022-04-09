'''
2. Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os demais
elementos (Matriz Identtidade). Escreva ao final a matriz obtida.
Saída:
1 0 0 0 0
0 1 0 0 0
0 0 1 0 0
0 0 0 1 0
0 0 0 0 1
'''
matriz = []
quantidade_maior_10 = 0
for i in range(5):
    linha = []
    for j in range(5):
        if i == j:
            linha.append(1)
        else:
            linha.append(0)

    matriz.append(linha)

# Mostrando a matriz
for linha in range(5):
    for coluna in range(5):
        print(matriz[linha][coluna], end=" ")
    print()