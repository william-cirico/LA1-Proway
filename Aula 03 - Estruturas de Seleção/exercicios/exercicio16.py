golsTime1 = int(input("Digite a quantidade de gols do time 1"))
golsTime2 = int(input("Digite a quantidade de gols do time 2"))

if (golsTime1 > golsTime2):
    print("O time 1 ganhou")
elif (golsTime1 < golsTime2):
    print("O time 2 ganhou")
else:
    print("O jogo empatou")