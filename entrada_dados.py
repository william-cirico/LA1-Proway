'''
Entrada de dados

A entrada de dados (INPUT) é feita através da função input
'''
input("Digite o seu nome: ")

# Se queremos armazenar o que foi digitado devemos atribuir o input a uma variável.
idade = input("Digite a sua idade: ")
print(idade)

# O que digitamos dentro de um input sempre será uma string:
print(type(idade))

# Portanto se precisarmos realizar alguma operação aritmética com o que digitamos será necessários fazer a conversão (cast) para o tipo adequado:
ano_atual = 2022
ano_nascimento = ano_atual - int(idade)

print(ano_nascimento)

# Mais exemplos de casting
x = str(3)   # x será '3' 
y = int(3)   # y será 3
z = float(3) # z será 3.0