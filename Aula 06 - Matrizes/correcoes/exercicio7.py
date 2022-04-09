'''
7.Leia uma matriz de 3 x 3 elementos. Calcule a soma dos elementos que estao na diagonal principal.
'''
matriz = []
soma = 0
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor  [ {i + 1} ] [ {j + 1} ] da matriz: "))
        linha.append(valor)

        if i > j:
            soma += valor

    matriz.append(linha)

print(f"Soma dos elementos que estão na diagonal principal: {soma}")