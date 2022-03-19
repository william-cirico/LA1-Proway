'''
Podemos controlar as estruturas de repetição através dos comandos break e continue

Normalmente o loop termina quando a condição se torna falsa. Porém nós conseguimos
forçar o fim do loop através do uso do break.
'''

soma: int = 0
while (True): # Loop infinito
    valor: int = int(input("Digite um número: ") or 0)

    if not valor:
        break

    soma += valor

print(f"Soma: {soma}")

# O continue é similar ao break, porém, quando ele é utilizado ele para somente a iteração
# atual e força o loop a começar a próxima iteração.
for i in range(10):
    if (i % 2 == 0):
        continue
    print(i)
