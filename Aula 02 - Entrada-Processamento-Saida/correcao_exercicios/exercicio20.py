# Escreva um script que receba a base e altura de triângulo e calcule a sua área.
# INPUT
# receba a base e altura de triângulo

# PROCESSAMENTO
# calcular a área do triângulo -> base * altura / 2

# OUTPUT
# Mostrar a área do triângulo
base: float = float(input("Digite a base do triângulo: "))
altura: float = float(input("Digite a altura do triângulo: "))

area: float = base * altura / 2

print(f"A área do triângulo é: {area:.2f}")
