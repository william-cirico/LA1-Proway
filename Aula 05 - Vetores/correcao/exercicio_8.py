"""
8) Crie um programa que leia 6 valores inteiros pares (GARANTA QUE ELES SEJAM PARES) e, em
seguida, mostre na tela os valores lidos na ordem inversa.
"""
valores = []
for i in range(6):
    while True:
        numero = int(input("Digite um valor par: "))
        if numero % 2 == 0:
            valores.append(numero)
            break
        
        print("Valor inválido!")
        

for i in valores[::-1]:
    print(i)
