'''
8. Faça um script que leia o nome e as notas de 3 alunos e armazene essas informações em
uma matriz no seguinte formato:
João   10   9   8
Maria  5    5   5 
Pedro  8    8   8

Após isso calcule a média de cada aluno e adicione a média na linha correspondente ao aluno
da matriz:
João   10   9   8   9
Maria  5    5   5   5
Pedro  8    8   8   8

Ao final mostre a matriz no formato abaixo e informe a situação dos alunos ("Aprovado" se a média for maior ou igual a 6
ou reprovado se for menor que 6).
Entrada:                  Saída:
João                      João   10   9   8   9  Aprovado
10                        Maria  5    5   5   5  Reprovado
9                         Pedro  8    8   8   8  Aprovado
8                         
Maria
5
5
5
Pedro
8
8
8
'''
matriz_alunos = []
for i in range(3):
    linha = []
    for j in range(4):
        valor = None
        if j == 0:
            valor = input("Digite o nome do aluno: ")
        else:
            valor = int(input(f"Digite a {j}ª nota do aluno: "))
        
        linha.append(valor)
    matriz_alunos.append(linha)

# Calculando a média e definindo a situação
for i, linha in enumerate(matriz_alunos):
    soma = 0
    for j, valor in enumerate(linha):
        if j > 0:
            soma += valor
    media = soma / 3
    linha.append(media)

    if media >= 6:
        linha.append("Aprovado")
    else:
        linha.append("Reprovado")

# Mostrando a matriz
for linha in matriz_alunos:
    for valor in linha:
        print(valor, end=" ")
    print()


