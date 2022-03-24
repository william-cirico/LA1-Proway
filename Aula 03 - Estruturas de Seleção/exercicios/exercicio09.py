valor_a = int(input("Digite o valor de A"))
valor_b = int(input("Digite o valor de B"))
valor_c = int(input("Digite o valor de C"))

if valor_a > valor_b and valor_a > valor_c:
    print(f"O maior número é: {valor_a}")
elif valor_b > valor_c:
    print(f"O maior número é: {valor_b}")
else:
    print(f"O maior número é {valor_c}")