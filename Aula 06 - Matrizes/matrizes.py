'''
Matrizes sã
'''
matriz = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

# Mostrando um elemento dentro de uma matriz
print(matriz[1][1])

# Mostrando uma matriz na tela
for linha in range(3):
    for coluna in range(3):
        print(matriz[linha][coluna], end=" ")
    print()

# Cadastrando valores em uma matriz
nova_matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor  [ {i + 1} ] [ {j + 1} ] da matriz: "))
        linha.append(valor)
    nova_matriz.append(linha)

print(nova_matriz)

