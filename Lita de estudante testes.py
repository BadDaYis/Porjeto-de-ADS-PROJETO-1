estudantes = []

professores = []

matriculas = []

turmas = []

def menu_estudantes():
    while True:
        print('\n ***** *Bem-Vindo ao Menu do *!ESTUDANTE!* *****')
        print('(1) Incluir   *Estudantes.')
        print('(2) Listar    *Estudantes.')
        print('(3) Atualizar *Estudantes.')
        print('(4) Excluir   *Estudantes.')
        print('(9) Voltar ao menu principal.')
        opcao = input('Informe a ação desejada:')


        if  opcao == '1':
            incluir_estudante()
        elif opcao == '2':
            listar_estudantes()
        elif opcao == '3':
            atualizar_estudante()
        elif opcao == '4':
            excluir_estudante()
        elif opcao == '9':
            print('♣voltando ao menu pricipal♣')
            break
        else:
            print("Opção inválida! tente novamente.")

def incluir_estudante():
    print('\n▬▬▬▬Inclusão▬▬▬▬')
    nome = input('Informe o nome do estudante:')
    estudantes.append(nome)
    print(f'Estudante Incluido')
    input('pressione ENTER para continuar.')

def listar_estudantes():
    print('\n▬▬▬▬ LISTAGEM ▬▬▬▬')
    if len(estudantes) == 0:
        print('Não há estudantes cadastrados.')
    else:
        for i, estudante in enumerate(estudantes):
            print(f'{i+1}. {estudante}')

    input("Pressione ENTER para continuar.")

def atualizar_estudante():
    listar_estudantes()
    if len(estudantes) > 0:
        try:
            indice = int(input('Informe o número do estudante que deseja excluir')) - 1
            if 0 <= indice < len(estudantes):
                novo_nome = input(f'informe o novo nome para {estudantes[indice]}: ')
                estudantes[indice] = novo_nome
                print('estudante atualizado com sucesso.')
            else:
                print('Estudante não encontrado.')
        except ValueError:
            print('Entrada inválida! por favor, informe um número válido.')
    input('Pressione ENTER para continuar.')

def excluir_estudante():
    listar_estudantes()
    if len(estudantes) > 0:
        try:
            indice = int(input('Informe o número do estudante que deseja Atualizar:')) -1
            if 0 <= indice < len(estudantes):
                removido = estudantes.pop(indice)
                print(f'Estudante {removido} excluído com sucesso.')
            else:
                print('Estudante não encontrado.')
        except ValueError:
            print('Entrada inválida! por favor, informe um número válido.')
    input('Pressione Enter para continuar.')

def menu_principal():
    while True:
        print('\n»»»» ♣♠♦MENU PRINCIPAL♦♠♣ ««««')
        print('(1) Estudantes.')
        print('(2) Profesores.')
        print('(3) Turmas.')
        print('(4) Matrícula.')
        print('(9) Sair.')
        opcao = input('Informe a ação desejada:')

        if opcao == '1':
            menu_estudantes()
        elif opcao == '2':
            menu_professores()
        elif opcao == '3':
            menu_turma()
        elif opcao == '4':
            menu_matricula()
        elif opcao == '9':
            print('Saindo....')
            break
        else:
            print('Opção inválida! Tente novamente.')



def menu_professores():
    while True:
        print('\n ***** ♠Bem-Vindo ao Menu do *!PROFESSOR!♠ *****')
        print('(1) Incluir    ♠Professores.')
        print('(2) Listar     ♠Professores.')
        print('(3) Atualizar  ♠Professores.')
        print('(4) Excluir    ♠Professores.')
        print('(9) Voltar ao menu principal.')
        opcao = input('Informe a ação desejada:')

        if opcao == '1':
            incluir_professor()
        elif opcao == '2':
            listar_professor()
        elif opcao == '3':
            atualizar_professor()
        elif opcao == '4':
            excluir_professor()
        elif opcao == '9':
            print('♣voltando ao menu pricipal♣')
            break
        else:
            print("Opção inválida! tente novamente.")


def incluir_professor():
    print('\n▬▬▬▬Inclusão▬▬▬▬')
    nome = input('Informe o nome do Professor:')
    professores.append(nome)
    print(f'Professor Incluido')
    input('pressione ENTER para continuar.')

def listar_professor():
    print('\n▬▬▬▬LISTAGEM▬▬▬▬')
    if len(professores) == 0:
        print('Não há Professores cadastrados.')
    else:
        for i, professor in enumerate(professores):
            print(f'{i+1}. {professor}')

    input("Pressione ENTER para continuar.")


def atualizar_professor():
    listar_professor()
    if len(professores) > 0:
        try:
            indice = int(input('Informe o número do professor que deseja Atualizar')) - 1
            if 0 <= indice < len(professores):
                novo_nome = input(f'informe o novo nome para {professores[indice]}: ')
                professores[indice] = novo_nome
                print('estudante atualizado com sucesso.')
            else:
                print('professor não encontrado.')
        except ValueError:
            print('Entrada inválida! por favor, informe um número válido.')
    input('Pressione ENTER para continuar.')

def excluir_professor():
    listar_professor()
    if len(professores) > 0:
        try:
            indice = int(input('Informe o número do Professor que deseja excluir:')) -1
            if 0 <= indice < len(professores):
                removido = professores.pop(indice)
                print(f'Professor {removido} excluído com sucesso.')
            else:
                print('Professor não encontrado.')
        except ValueError:
            print('Entrada inválida! por favor, informe um número válido.')
    input('Pressione Enter para continuar.')



def menu_matricula():
    while True:
        print('\n ***** ♣Bem-Vindo ao Menu de *!MATRICULAS!♣ *****')
        print('(1) Incluir    ♣Matricula.')
        print('(2) Listar     ♣Matriculas.')
        print('(3) Atualizar  ♣Matricula.')
        print('(4) Excluir    ♣Matricula.')
        print('(9) Voltar ao menu principal.')
        opcao = input('Informe a ação desejada:')

        if opcao == '1':
            incluir_matricula()
        elif opcao == '2':
            listar_matricula()
        elif opcao == '3':
            atualizar_matricula()
        elif opcao == '4':
            excluir_matricula()
        elif opcao == '9':
            print('♣voltando ao menu pricipal♣')
            break
        else:
            print("Opção inválida! tente novamente.")


def incluir_matricula():
    print('\n▬▬▬▬Inclusão▬▬▬▬')
    nome = input('Informe o nome do Professor:')
    matriculas.append(nome)
    print(f'Professor Incluido')
    input('pressione ENTER para continuar.')

def listar_matricula():
    print('\n▬▬▬▬ LISTAGEM ▬▬▬▬')
    if len(matriculas) == 0:
        print('Não há matricula cadastradas.')
    else:
        for i, matricula in enumerate(matriculas):
            print(f'{i+1}. {matricula}')

    input("Pressione ENTER para continuar.")


def atualizar_matricula():
    listar_matricula()
    if len(matriculas) > 0:
        try:
            indice = int(input('Informe o número da Matricula que deseja Atualizar')) - 1
            if 0 <= indice < len(matriculas):
                novo_nome = input(f'informe o novo nome para {matriculas[indice]}: ')
                matriculas[indice] = novo_nome
                print('Matricula atualizada com sucesso.')
            else:
                print('Matricula não encontrada.')
        except ValueError:
            print('Entrada inválida! por favor, informe um número válido.')
    input('Pressione ENTER para continuar.')

def excluir_matricula():
    listar_matricula()
    if len(matriculas) > 0:
        try:
            indice = int(input('Informe o número da Matricula que deseja excluir:')) -1
            if 0 <= indice < len(matriculas):
                removido = matriculas.pop(indice)
                print(f'Matricula {removido} excluída com sucesso.')
            else:
                print('Matricula não encontrada.')
        except ValueError:
            print('Entrada inválida! por favor, informe um número válido.')
    input('Pressione Enter para continuar.')


def menu_turma():
    while True:
        print('\n ***** ♦Bem-Vindo ao Menu de *!TURMAS!♦ *****')
        print('(1) Incluir   - Turma.')
        print('(2) Listar    - Turmas.')
        print('(3) Atualizar - Turma.')
        print('(4) Excluir   - Turma.')
        print('(9) Voltar ao menu principal.')
        opcao = input('Informe a ação desejada:')

        if opcao == '1':
            incluir_turma()
        elif opcao == '2':
            listar_turma()
        elif opcao == '3':
            atualizar_turma()
        elif opcao == '4':
            excluir_turma()
        elif opcao == '9':
            print('♣voltando ao menu pricipal♣')
            break
        else:
            print("Opção inválida! tente novamente.")



def incluir_turma():
    print('\n▬▬▬▬Inclusão▬▬▬▬')
    nome = input('Informe o nome da Turma:')
    turmas.append(nome)
    print(f'Professor Incluido')
    input('pressione ENTER para continuar.')

def listar_turma():
    print('\n▬▬▬▬ LISTAGEM ▬▬▬▬')
    if len(turmas) == 0:
        print('Não há Turma cadastradas.')
    else:
        for i, turma in enumerate(turmas):
            print(f'{i+1}. {turma}')

    input("Pressione ENTER para continuar.")


def atualizar_turma():
    listar_turma()
    if len(turmas) > 0:
        try:
            indice = int(input('Informe o número da Turma que deseja Atualizar')) - 1
            if 0 <= indice < len(turmas):
                novo_nome = input(f'informe o novo nome para {turmas[indice]}: ')
                turmas[indice] = novo_nome
                print('Turma atualizada com sucesso.')
            else:
                print('Turma não encontrada.')
        except ValueError:
            print('Entrada inválida! por favor, informe um número válido.')
    input('Pressione ENTER para continuar.')

def excluir_turma():
    listar_turma()
    if len(turmas) > 0:
        try:
            indice = int(input('Informe o número da Turma que deseja excluir:')) -1
            if 0 <= indice < len(turmas):
                removido = turmas.pop(indice)
                print(f'Turma {removido} excluída com sucesso.')
            else:
                print('Turma não encontrada.')
        except ValueError:
            print('Entrada inválida! por favor, informe um número válido.')
    input('Pressione Enter para continuar.')


def menu_turma():
    while True:
        print('\n ***** ♦Bem-Vindo ao Menu de *!TURMAS!♦ *****')
        print('(1) Incluir    ♦Turma.')
        print('(2) Listar     ♦Turmas.')
        print('(3) Atualizar  ♦Turma.')
        print('(4) Excluir    ♦Turma.')
        print('(9) Voltar ao menu principal.')
        opcao = input('Informe a ação desejada:')

        if opcao == '1':
            incluir_turma()
        elif opcao == '2':
            listar_turma()
        elif opcao == '3':
            atualizar_turma()
        elif opcao == '4':
            excluir_turma()
        elif opcao == '9':
            print('♣voltando ao menu pricipal♣')
            break
        else:
            print("Opção inválida! tente novamente.")


menu_principal()






