totalVotosJose = 0
totalVotosMaria = 0
totalVotosJoao = 0
totalNulos = 0
totalBranco = 0

while (True):
    voto = int(input("Em quem você vota?\n1 - José Bolinha\n2 - Maria Nascimento\n3 - João da Silva\n4 - Voto Nulo\n5 - Voto em branco\nDigite o seu voto: "))
    
    if voto == 0:
        break

    if voto == 1:              
        totalVotosJose += 1
    elif voto == 2:
        totalVotosMaria += 1
    elif voto == 3:
        totalVotosJoao += 1
    elif voto == 4: 
        totalNulos += 1
    elif voto == 5:
        totalBranco += 1
    else:
        print("Opção inválida")

print(f"Total de Votos\nJosé Bolinha: {totalVotosJose} voto(s)\nMaria Nascimento: {totalVotosMaria} voto(s)\nJoão da Silva: {totalVotosJoao} voto(s)\nVotos Nulos: {totalNulos} voto(s)\nVotos em Branco: {totalBranco} voto(s)")