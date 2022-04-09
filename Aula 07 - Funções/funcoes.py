'''
Funções

Sintaxe de uma função:

def nome_funcao(parametro1, parametro2...):
    # corpo da função
'''
def lava_a_louca():
    print("William está lavando a louça")

def limpa_o_chao():
    print("Alexandre está limpando o chão")

def faz_comida():
    print("Alison está fazendo comida")

def dobro(numero: int) -> int:
    '''Retorna o dobro de um número'''
    return numero * 2

print(dobro(10)) # Quando o valor é retornado podemos armazenar ele em uma variável ou mostrar ele na tela

def soma(a: int, b: int = 10) -> int:
    '''Retorna a soma entre a e b. Se nenhum valor for informado para b, irá utilizar 10'''
    return a + b


