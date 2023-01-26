agenda = {}
loop = True

def incluirNovoNome():
    numTelefones = int(input("Quantos números deseja salvar? "))
    contato = str(input("Digite o nome a ser gravado na agenda: "))
    agenda[contato] = []
    for i in range(0,numTelefones):
        telefone = int(input(f"Digite o {i+1}º numero que deseja gravar: "))
        agenda[contato].append(telefone)

def incluirTelefone():
    contato = str(input("Deseja incluir o telefone em qual contato da lista?"))
    if contato in agenda:
        telefone = int(input("Digite o novo número: "))
        agenda[contato].append(telefone)
    else:
        novoContato = input("Esse contato não existe! Deseja adicionar(s/n):")
        if novoContato == "s":
            incluirNovoNome()

def excluirTelefone():
    contato = input("Deseja excluir o número telefônico de quem?")
    if contato in agenda:
        excluido = agenda[contato].pop()
        print(f"Número telefônico {excluido} de {contato} excluido com sucesso!")
        if len(agenda[contato]) == 0:
            agenda.pop(contato)
            print(f"O contato {contato} possuia apenas um número e, por isso, foi removido da agenda.")
    else:
        print("Contato inexistente!")

def excluirNome():
    contato = input("Deseja excluir qual contato?")
    if contato in agenda:
        agenda.pop(contato)
        print(f"O contato {contato} foi removido com sucesso!")
    else:
        print("Contato inexistente!")

def consultarTelefone():
    contato = input("Deseja consultar o(s)telefone(s) de qual contato? ")
    if contato in agenda:
        print(f"Aqui está {agenda[contato]}.")
    else:
        print("Contato inexistente!")

print("Bem-vindo à sua Agenda!")
while loop:
    print(" ")
    print("O que deseja fazer?")
    print("1 - Adicionar novo contato.")
    print("2 - Adicionar novo número em contato existente.")
    print("3 - Excluir um número ou um contato (caso o contato possua apenas um número).")
    print("4 - Excluir um contato.")
    print("5 - Consultar números de um contato salvo.")
    print("6 - Mostrar a agenda completa.")
    print("7 - Sair")
    try:
        resposta = int(input("Dê o comando (apenas o número): "))
        if resposta == 1:
            incluirNovoNome()
            continue

        elif resposta == 2:
            incluirTelefone()
            continue

        elif resposta == 3:
            excluirTelefone()
            continue

        elif resposta == 4:
            excluirNome()
            continue

        elif resposta == 5:
            consultarTelefone()
            continue

        elif resposta == 6:
            if len(agenda) == 0:
                print("Agenda vazia!")
            else:
                print(agenda)
            continue

        elif resposta == 7:
            loop = False
            input("Tchau!")
    except:
        print("Dê uma resposta válida!")
        continue