maior_valor, menor_valor = None, None
for i in range(5):
    valor = int(input("Digite um valor: "))

    if i == 0:
        maior_valor = valor
        menor_valor = valor
    elif valor > maior_valor:
        maior_valor = valor
    elif valor < menor_valor:
        menor_valor = valor

print(maior_valor, menor_valor)