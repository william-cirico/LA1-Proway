# 14)Faça um programa que receba duas notas do usuário, 
# calcule a média e mostre o resultado na tela.
# INPUT
# N1, N2

# PROCESSAMENTO
# Calcular a média = (N1 + N2) / 2

# OUTPUT
# Média
nota1: float = float(input("Digite a nota 1: "))
nota2: float = float(input("Digite a nota 2: "))

media: float = (nota1 + nota2) / 2

print(f"A média é: {media:.2f}")