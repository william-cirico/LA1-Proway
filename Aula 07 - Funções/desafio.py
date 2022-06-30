import os

alunos = []

def mostrar_menu():
    """Mostra o menu principal."""
    print("Sistema de Gestão de Alunos\n1) Cadastrar aluno\n2) Editar informações do aluno\n3) Cadastrar notas de um aluno\n4) Listar alunos\n0) Sair")


def cadastrar_aluno():
    """Cadastra os alunos na matriz de alunos."""
    global alunos
    matricula = input("Digite a matrícula do aluno: ")

    if matricula_ja_cadastrada(matricula):
        input(f"Já existe um aluno cadastrado com essa matrícula: {matricula}")
        return

    nome = input("Digite o nome do aluno: ")

    aluno = [matricula, nome, "--", "--", "--", "--"]
    alunos.append(aluno)
    input("Aluno cadastrado com sucesso! 😉")


def matricula_ja_cadastrada(matricula: str) -> bool:
    """Verifica se a matrícula já está cadastrada."""
    for aluno in alunos:
        if aluno[0] == matricula:
            return True
    
    return False


def editar_aluno():
    """Edita o aluno."""
    global alunos

    matricula = input("Digite a matrícula do aluno: ")

    indice_aluno = obtem_aluno(matricula)
    if indice_aluno < 0:
        input("Não existe um aluno com a matrícula informada. 😢")
        return

    nome = input("Digite o novo nome do aluno: ")
    alunos[indice_aluno][1] = nome
    input("Nome alterado com sucesso. 😁")


def obtem_aluno(matricula: str) -> int:
    """Retorna o índice do aluno na matriz de alunos, ou -1 caso o índice não exista."""
    global alunos
    for i, aluno in enumerate(alunos):
        if aluno[0] == matricula:
            return i
    
    return -1


def cadastrar_notas():
    """Cadastrar as notas de um aluno"""
    global alunos

    matricula = input("Digite a matrícula do aluno: ")

    indice_aluno = obtem_aluno(matricula)
    if indice_aluno < 0:
        input("Não existe um aluno com a matrícula informada. 😢")
        return
    
    # Cadastrando as notas
    soma = 0
    for i in range(1, 4):
        nota = float(input(f"Digite a {i} nota: "))
        soma += nota

        # Adicionando a nota na linha do aluno
        alunos[indice_aluno][i + 1] = nota
        
    # Calculando a média
    media = soma / 3

    # Adicionando a média na linha do aluno
    alunos[indice_aluno][5] = media

def listar_alunos():
    """Lista todos os alunos"""
    for aluno in alunos:
        for coluna in aluno:
            print(coluna, end="  ")
        print()
    input("Pressione qualquer tecla para continuar. 😁")

while True:
    os.system("cls")
    mostrar_menu()

    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        cadastrar_aluno()
    elif opcao == 2:
        editar_aluno()
    elif opcao == 3:
        cadastrar_notas()
    elif opcao == 4:
        listar_alunos()
    elif opcao == 0:
        break
    else:
        input("Opção inválida")
