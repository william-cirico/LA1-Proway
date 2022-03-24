numero_a = int(input("Digite o número A: "))
numero_b = int(input("Digite o número B: "))
numero_c = int(input("Digite o número C: "))

if numero_c > numero_b:
    aux = numero_c
    numero_c = numero_b
    numero_b = aux

if numero_b > numero_a:
    aux = numero_b
    numero_b = numero_a
    numero_a = aux

if numero_c > numero_b:
    aux = numero_c
    numero_c = numero_b
    numero_b = aux

print(numero_a, numero_b, numero_c)