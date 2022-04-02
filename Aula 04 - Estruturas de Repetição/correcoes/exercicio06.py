soma = 0
for i in range(5):
    valor = int(input(f"Digite o {i + 1} valor: "))

    soma += valor

media = soma / 5

print(f"Soma: {soma}")
print(f"Média: {media:.2f}")