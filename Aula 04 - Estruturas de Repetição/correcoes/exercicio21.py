contador_numeros_primos = 0
numero_atual = 2    
flag = False
primos = ""

while (contador_numeros_primos < 20):         
    for i in range(2, numero_atual):
        if numero_atual % i == 0:
            flag = True
            break

    if not flag:
        primos += f"{numero_atual} "
        contador_numeros_primos += 1

    flag = False
    numero_atual += 1

print(primos)