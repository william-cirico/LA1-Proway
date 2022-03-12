# INPUT
altura: float = float(input("Digite a altura do retângulo: "))
largura: float = float(input("Digite a largura do retângulo: "))

# PROCESSAMENTO
area: float = altura * largura
perimetro: float = altura * 2 + largura * 2

# OUTPUT
print(f"""
A área do retângulo é: {area:.2f}
O perímetro do retângulo é: {perimetro:.2f}
""")


