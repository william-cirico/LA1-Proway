quantidade_negativos = 0
for i in range(5):
    numero = int(input("Digite um número: "))
    
    if numero < 0:
        quantidade_negativos += 1

print(quantidade_negativos)