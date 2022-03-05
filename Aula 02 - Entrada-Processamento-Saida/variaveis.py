'''
As variáveis são espaços na memória utilizados para armazenar informações que o programa precisa para funcionar.

Regras de nomenclatura das variáveis:
    * Não pode iniciar com símbolos (com exceção do _ ) ou números.
    * Cada nova palavra que compõe a variável deve ser separada por _.
    * Os nomes das variáveis devem ser descritíveis. Qualquer pessoa deve ser capaz de saber o que irá ser armazenado dentro dela.
'''

nome: str = "João" # Declarando uma variável do tipo string
idade: int = 26 # Declarando uma variável do tipo inteiro
altura: float = 1.82 # Declarando uma variável do tipo float
presente: bool = False # Declarando uma variável do tipo bool

# Como saber o tipo de uma variável:
print(type(nome))

# Trocando os valores de uma variável:
a: int = 1
b: int = 2
auxiliar: int = a
a = b
b = auxiliar
print(a, b)

# Em python podemos fazer isso de outra forma:
c, d = 1, 2 # Declarando várias variáveis em uma única linha
print(c, d)
c, d = d, c
print(c, d)

# String Literal:
nome_cachorro = "snoopy"
print(f"O nome do cachorro é: {nome_cachorro}")

# Arredondando valores com string literal:
valor_decimal = 9.726348712663278616423168234678426789
print(f"O valor arrendodado para duas casas decimais é: {valor_decimal:.2f}")
