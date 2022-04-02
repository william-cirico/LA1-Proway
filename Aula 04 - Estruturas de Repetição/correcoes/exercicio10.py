quantidade_pares, quantidade_impares = 0, 0

for i in range(10):
    numero = int(input(f"Digite o {i + 1} número: "))

    if numero % 2 == 0:
        quantidade_pares += 1
    else:
        quantidade_impares += 1

print(f"Pares: {quantidade_pares}")
print(f"Ímpares: {quantidade_impares}")