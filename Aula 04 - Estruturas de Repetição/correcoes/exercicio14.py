numero = int(input("Digite um número: "))
fatoracao = numero

for i in range(numero - 1, 0, -1):
    fatoracao *= i

print(f"O fator de {numero} é: {fatoracao}")