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

10 > 5   # ?
2 < 5    # ?
10 >= 2  # ?
10 <= 11 # ?
10 != 5  # ?
not 3    # ?

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
'''
# Estrutura de seleção simples
if (1 > 10):
    print("Um é maior que dez")

if (1 <= 10):
    print("Um é menor ou igual a dez")

# Podemos utilizar variáveis nas estruturas de seleção:
valor: int = 10
if valor == 10:
    print("O valor armazenado dentro da variável valor é igual a 10")

# Estrutura de seleção composta
if valor > 10:
    print("O número é maior que 10")
else:
    print("O número é menor ou igual a 10")

# Estrutura de seleção múltipla
if valor < 10:
    print("O número é menor que 10")
elif valor > 10:
    print("O número é maior que 10")
else:
    print("O número é igual a 10")

# Utilizando os operadores lógicos
numero = 11
if numero > 10 and numero < 90:
    print("O número é maior que 10 e menor do que 90")

if numero > 20 or numero < 90:
    print("O número é maior que 20 ou menor que 90")

# Operador ternário
print("O número é maior que 10") if valor > 10 else print("O número é menor ou igual a 10")





