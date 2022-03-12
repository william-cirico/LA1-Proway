# Considerando que cada mês possui 30 dias, faça um algoritmo que:

# Receba uma quantidade n de meses do usuário.
# Calcule o total de dias com base nessa quantidade n de meses.
# Mostre o resultado na tela.

# INPUT
# Quantidade de meses (n)

# PROCESSAMENTO
# Calcule o total de dias -> 30 * n

# OUTPUT
# Mostrar a quantidade de dias

# CONSTANTE -> Uma "variável" que não pode ser alterada
DIAS_NO_MES: int = 30

# INPUT
n: int = int(input("Digite a quantidade de meses: "))

# PROCESSAMENTO
total_dias = n * DIAS_NO_MES

#  OUTPUT
print(f"A quantidade de dias em {n} meses é: {total_dias}")
