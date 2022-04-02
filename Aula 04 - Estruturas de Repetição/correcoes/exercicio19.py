while True:
    matricula = int(input("Qual a matricula do aluno? "))
    if matricula == 0:
        break

    nota1 = float(input("Qual a primeira nota? "))
    nota2 = float(input("Qual a segunda nota? "))
    nota3 = float(input("Qual a terceira nota? "))

    media = (nota1 + nota2 + nota3) / 3

    print(f"A média do aluno com a matricula {matricula} é {media:.2f}")