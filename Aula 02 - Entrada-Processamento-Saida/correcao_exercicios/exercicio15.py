# Faça um programa que receba 3 números, calcule o quadrado de cada um deles e 
# mostre o resultado na tela.
# INPUT
# N1, N2, N3

# PROCESSAMENTO
# quadrado de cada um deles (N1, N2, N3)

# OUTPUT
# Mostrar o resultado

# INPUT
numero1: int = int(input("Digite o número 1: "))
numero2: int = int(input("Digite o número 2: "))
numero3: int = int(input("Digite o número 3: "))

# PROCESSAMENTO
quadrado1: int = numero1 ** 2
quadrado2: int = numero2 ** 2
quadrado3: int = numero3 ** 2

# OUTPUT
print(f"""
O quadrado número {numero1} é: {quadrado1}
O quadrado número {numero2} é: {quadrado2}
O quadrado número {numero3} é: {quadrado3}
""")
