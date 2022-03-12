# Escreva um algoritmo que armazene o valor 10 em uma variável A 
# e o valor 20 em uma variável B. A seguir 
# (utilizando apenas atribuições entre variáveis) troque os seus conteúdos 
# fazendo com que o valor que está em A passe para B e vice-versa. Ao final, 
# mostrar na tela os valores que ficaram armazenados nas variáveis.
a: int = 10
b: int = 20
aux: int = a

a = b
b = aux

# a, b = b, a
print(a, b)

