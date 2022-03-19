'''
Em python o laço de repetição for requer a utilização de um Iterable.

Um Iterable é uma coleção que possui vários valores.
O Iterable que vamos utilizar para construir o nosso laço de repetição é
o range().

A função range(x) cria uma sequência de números de acordo com o valor x.

Portanto se utilizarmos o comando range(10), teremos a seguinte coleção:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9 -> Sempre começa em 0.
'''
from os import sep


for i in range(10):
    print(f"O laço está repetindo pela {i + 1} vez")

# A função range aceita o valor inicial e o passo:
# range(valor_inicial, valor_final, passo)
for i in range(1, 10, 2):
    print(i)

# Se quisermos exibir o resultado na mesma linha:
for i in range(10):
    print(i, end=" ")