'''
Estruturas de Seleção

Estruturas de seleção ou estruturas condicionais são responsáveis por desviar
o fluxo de execução do algoritmo baseado em uma condição que sempre será
VERDADEIRA OU FALSA. Portando, o tipo de dado utilizado em estruturas de seleção
é o booleano.

Para fazermos as comparações necessárias em uma estrutura de seleçao,
podemos utilizar os seguintes operadores de comparação:
    >    ->  Maior que
    <    ->  Menor que
    >=   ->  Maior ou igual a
    <=   ->  Menor ou igual a
    !=   ->  Diferente de
    not  ->  Negação

Quando utilizamos esses operadores para comparar valores o resultado sempre
será um booleano, ou seja, True ou False (Verdadeiro ou Falso).

Estrutura de seleção simples:
if condicao:
    # Instruções caso a condição seja verdadeira

Estrutura de seleção composta:
if condicao:
    # Instruções caso a condição seja verdadeira
else:
    # Instruções caso a condição seja falsa

Estrutura de seleção múltipla:
if condicao1:
    # Instruções caso a condição1 seja verdadeira
elif condicao2:
    # Instruções caso a condição2 seja verdadeira
else:
    # Instruções caso as condições anteriores sejam falsas

# Extra
A maioria das linguagens possui uma forma de escrever a estrutura de seleção composta em apenas uma linha.
Essa forma se chama **Operador Ternário**.

Em Python a sintaxe de um operador ternário é a seguinte:
valor_se_verdadeiro if condicao else valor_se_falso

10 > 10 # False
21 < 2 # False
21 >= 10 # True
92 <= 100 # True
80 <= 79 # False
not 80 # False
'''

# Escopo de variáveis
numero: int = 10
if 1 < 10:
    numero = 20
    print("O número é maior que 10")

print(numero)

# Estrutura de seleção simples
if (1 > 10):
    print("Um é maior que dez")

if (1 <= 10):
    print("Um é menor ou igual a dez")

# Estrutura de seleção composta
valor: int = 20
if valor > 10:
    print("O valor é maior que 10")
else:
    print("O valor é menor ou igual a 10")

# Estrutura de seleção múltipla
if valor < 10:
    print("O número é menor que 10")
elif valor > 10:
    print("O número é maior que 10")
else:
    print("O número é igual a 10")

numero: int = 8
if numero > 10:
    if numero <= 8:
        print("O número é menor que 8")

    print("O valor é maior que 10")
elif numero == 10:
    print("O valor é igual a 10")
elif numero == 8:
    print("O valor é igual a 8")
else:
    print("O valor é menor que 10")



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

# Utilizando os operadores lógicos
outro_numero: int = 30
if outro_numero > 100 or outro_numero < 200: 
    print("Outro número é maior que 100 e menor que 200")

if (outro_numero >= 30 or outro_numero < 200) and outro_numero > 100:
    print("Outro número é maior ou igual a 30 e menor que 200")

# Operador ternário
# if valor > 10:
#     print("O valor é maior que 10")
# else:
#     print("O valor é menor ou igual a 10")
# <intruções caso verdadeiro> if <condicao> else <intruções caso falso>
valor = 10
print("O valor é maior que 10") if valor < 10 else print("O valor é menor ou igual a 10")

dia_da_semana: int = 2
# Switch em Python
if (dia_da_semana == 1):
    print("Domingo")
elif (dia_da_semana == 2):
    print("Segunda")
elif (dia_da_semana == 7):
    print("Sábado")
else:
    print("Dia da semana é inválido")

# Para obter a raiz quadrada: math.sqrt()