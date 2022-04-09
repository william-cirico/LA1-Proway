'''
9. Utilizando os conceitos de matrizes e laços de repetição faça um jogo da velha
onde a cada rodada será pedido a posição onde o jogador A quer jogar e onde o jogador
B quer jogar. Caso seja informado uma posição já ocupada, informe que a "posição já está ocupada"
e peça por outra jogada. Quando o jogo acabar mostrar quem ganhou o jogo, ou em caso de empate, a
mensagem: "O jogo empatou".
'''
import os


jogo_da_velha = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
];

jogadas = 0
jogador_atual = 1
ganhou = False
while True:
    # Limpando a tela
    os.system("cls")

    # Mostrando o tabuleiro
    for linha in jogo_da_velha:
        for valor in linha:
            if valor == 0:
                print("-", end="  ")
            elif valor == 1:
                print("X", end="  ")
            else:
                print("O", end="  ")
        print()

    # Verificando se ganhou
    if ganhou:
        print("O jogador 1 ganhou") if jogador_atual == 1 else print("O jogador 2 ganhou")
        break

    # Verificando o empate
    if (jogadas == 9):
        print("Empatou")
        break

    print("Jogador 1") if jogador_atual == 1 else print("Jogador 2")
    linha_jogada = int(input("Digite a linha: "))
    coluna_jogada = int(input("Digite a coluna: "))

    if jogo_da_velha[linha_jogada][coluna_jogada] != 0:
        input("Posição já está ocupada")
        continue

    jogo_da_velha[linha_jogada][coluna_jogada] = jogador_atual

    # Checando linhas
    for i in range(3):
        soma = jogo_da_velha[i][0] + jogo_da_velha[i][1] + jogo_da_velha[i][2]
        if soma == 3 or soma == -3:
            ganhou = True

     # Checando colunas
    for i in range(3):
        soma = jogo_da_velha[0][i] + jogo_da_velha[1][i] + jogo_da_velha[2][i]
        if soma == 3 or soma == -3:
            ganhou = True

    # Checando diagonais
    diagonal1 = jogo_da_velha[0][0] + jogo_da_velha[1][1] + jogo_da_velha[2][2]
    diagonal2 = jogo_da_velha[0][2] + jogo_da_velha[1][1] + jogo_da_velha[2][0]
    if diagonal1 == 3 or diagonal1 == -3 or diagonal2 == 3 or diagonal2 == -3:
        ganhou = True

    # Aumentando o número de jogadas
    jogadas += 1

    # Trocando o jogador
    jogador_atual = -jogador_atual

    
