"""
2) Escreva um programa que leia 5 numeros e os armazene em um vetor. 
Mostre o vetor, o maior elemento e a posição que ele se encontra.
"""
valores = []
maior = 0
posicao = 0
for i in range(5):
    valor = int(input(f"Digite o {i + 1}º valor: "))
    valores.append(valor)
    if i == 0:
        maior = valor
    elif valor > maior:
        maior = valor
        posicao = i
print(valores)
print(f"O maior valor é {maior} e é o {posicao}")