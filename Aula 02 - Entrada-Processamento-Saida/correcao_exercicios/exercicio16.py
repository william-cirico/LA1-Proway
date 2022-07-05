# Elabore um script que leia um número e 
# apresente o antecessor, o número e o sucessor.
numero: int = int(input("Digite um número inteiro: "))

antecessor = numero - 1
sucessor = numero + 1

print(antecessor, numero, sucessor)