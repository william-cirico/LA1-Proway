'''
Operadores aritméticos são utilizados para executar as operações do algoritmo.

Operadores básicos:
    * Adição: +
    * Subtração: -
    * Multiplicação: *
    * Divisão: /
    * Divisão inteira: //
    * Módulo (obter o resto): %
    * Exponeciação: **    

Operadores de atribuição:
    * +=: x += 3 -> x = x + 3
    * -=: x -= 3 -> x = x - 3
    * *=: x *= 3 -> x = x * 3
    * /=: x /= 3 -> x = x / 3
    * //=: x //= 3 -> x = x // 3
    * %=: x %= 3 -> x = x % 3    
    * **=: x **= 3 -> x = x ** 3

Precedência de operadores:
    1. Agrupamento -> ()
    2. Exponenciação -> **
    3. Multiplicação, Divisão e Resto -> *, /, %
    4. Adição e subtração -> +, -
'''

a = 1
a += 3
print(a)

b = 3
b -= 3
print(b)

c = 3
c *= 3
print(c)

d = 6
d /= 2
print(d)

e = 3
e //= 2
print(e)

f = 3
f %= 2
print(f)

g = 3
g **= 2
print(g)

