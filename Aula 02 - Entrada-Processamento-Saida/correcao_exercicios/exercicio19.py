# Faça um programa que calcule e mostre o volume de uma esfera sendo 
# fornecido o valor de seu raio R. A fórmula para calcular o 
# volume é: (4/3) * pi * R^3. Considere (atribua) para pi o valor 3.14159.
import math


PI = 3.14159
R: float = float(input("Digite o valor do raio: "))

volume: float = 4 / 3 * math.pi * R ** 3

print(f"O volume da esfera é: {volume:.2f}")

