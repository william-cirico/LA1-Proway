for i in range(5):
    media = int(input("Digite a média: "))

    if media < 0 or media > 10:
        print("Valor inválido")
    elif media < 5 and media >= 0:
        print("Conceito D")
    elif media < 7:
        print("Conceito C")
    elif media < 9:
        print("Conceito B")
    else:
        print("Conceito A")
    
