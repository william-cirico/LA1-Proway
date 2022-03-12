'''
> -> Maior que
< -> Menor que
>= -> Maior ou igual a
<= -> Menor ou igual a
!= -> Diferente de
== -> Igual a
not -> Negação

10 > 10 # False
21 < 2 # False
21 >= 10 # True
92 <= 100 # True
80 <= 79 # False
not 80 # False
'''

# Escopo de variáveis
# numero: int = 10
if 1 < 10:
    numero = 20
    print("O número é maior que 10")

print(numero)
valor: int = 20
if valor > 10:
    print("O valor é maior que 10")
else:
    print("O valor é menor ou igual a 10")

# print("Finalizou...")

# numero: int = 8
# if numero > 10:
#     if numero <= 8:
#         print("O número é menor que 8")

#     print("O valor é maior que 10")
# elif numero == 10:
#     print("O valor é igual a 10")
# elif numero == 8:
#     print("O valor é igual a 8")
# else:
#     print("O valor é menor que 10")

# outro_numero: int = 30

# AND
# a | b | a and b
# V | V | V 
# V | F | F
# F | V | F
# F | F | F

# OR
# a | b | a or b
# V | V | V 
# V | F | V
# F | V | V
# F | F | F

# if outro_numero > 100 or outro_numero < 200: 
#     print("Outro número é maior que 100 e menor que 200")

# if (outro_numero >= 30 or outro_numero < 200) and outro_numero > 100:
#     print("Outro número é maior ou igual a 30 e menor que 200")

valor: int = 20
# if valor > 10:
#     print("O valor é maior que 10")
# else:
#     print("O valor é menor ou igual a 10")
# <intruções caso verdadeiro> if <condicao> else <intruções caso falso>
print("O valor é maior que 10") if valor < 10 else print("O valor é menor ou igual a 10")
