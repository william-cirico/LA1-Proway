quantidade_no_intervalo = 0
quantidade_fora_intervalo = 0
while True:
    numero = int(input("Digite um número: "))

    if numero < 0:
        break

    if 10 >= numero <= 20:
        quantidade_no_intervalo += 1
    else:
        quantidade_fora_intervalo += 1
    
print(f"Quantidade de números no intervalo: {quantidade_no_intervalo}")
print(f"Quantidade de números fora do intervalo: {quantidade_fora_intervalo}")