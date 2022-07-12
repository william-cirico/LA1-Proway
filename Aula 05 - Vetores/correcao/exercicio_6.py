"""
6) Faça um programa que possua um vetor denominado A que armazene 6 numeros inteiros.
O programa deve executar os seguintes passos:

(a) Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 7.
(b) Armazene em uma variavel a soma entre os valores das posições A[0], 
A[1] e A[5] do vetor e mostre na tela esta soma.
(c) Modifique o vetor na posição 4, atribuindo a esta posição o valor 100.
(d) Mostre na tela cada valor do vetor A, um em cada linha.
"""

"""(a) Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 7.
"""
vetor = [1, 0, 5, -2, -5, 7]

"""
(b) Armazene em uma variavel a soma entre os valores das posições A[0],
A[1] e A[5] do vetor e mostre na tela esta soma. 
"""
vetor = [1, 0, 5, -2, -5, 7]

soma = vetor[0] + vetor[1] + vetor[5]

print(soma)

"""
(c) Modifique o vetor na posição 4, atribuindo a esta posição o valor 100.
"""
vetor = [1, 0, 5, -2, -5, 7]

vetor[4] = 100

"""
(d) Mostre na tela cada valor do vetor A, um em cada linha.
"""

for item in vetor:
    print(item)
