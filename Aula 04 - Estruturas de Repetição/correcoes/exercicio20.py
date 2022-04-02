menor_numero = int(input("O menor número: "))
maior_numero = int(input("Digite o maior número: "))
soma_par = 0
multiplica_impar = 1

for i in range(menor_numero, maior_numero + 1):  
    if i % 2 == 0:
        soma_par += i 
    else:
        multiplica_impar *= i       

print(f"Soma dos pares: {soma_par}\nMultiplição dos Impares: {multiplica_impar}")