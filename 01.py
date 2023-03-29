def menu_ocorrencias(lista_ocorrencias):
    opcao = 1
    while opcao != 0:
        print("---Menu de Ocorrências---")    
        print("1 - Cadastro de Ocorrências---")
        print("2 - Listar todas Ocorrências---")
        print("3 - Listar todas Ocorrências ativas")
        print("0 - Sair")
        opcao = int(input("Entre com a opção>>"))
        if opcao == 1:
            print("---Cadastro---")
            cadastro(lista_ocorrencias)
        elif opcao == 2:
            print("---Listagem---")
            listagem(lista_ocorrencias)
        elif == 3:
            print("---Listagem[ATIVAS]")
            listagem_ativas(lista_ocorrencias)
        elif opcao == 0:
            print("Saindo do programa!!!")
        else:
            print("Opção Inválida!")

def cadastro(lista_ocorrencias):
    titulo = input("Entre com o titulo da ocorrência:")
    descricao = input("Entre com o descrição da ocorrência:")
    implicacoes = input("Entre com as implicações da ocorrência:")
    em_atividade = input ("Está em atividade? (sim|não)")
    status = True if em_atividade =="sim"else False
    prazo = int(input("Entre com a estimativa de prazo em dias:"))
    ocorrencia = dict(titulo = titulo, descricao = descricao, implicacoes = implicacoes, em_atividade = em_atividade, status = status, prazo = prazo )
    lista_ocorrencias.append(ocorrencia)
    print("Ocorrência cadastrada com sucesso!")

def listagem(lista_ocorrencias):
    tamanho = len(lista_ocorrencias)
    if tamanho > 0:
        print("---Listagem de todas as ocorrências---")
        for i in range(tamanho):
            print("### Ocorrência" , i + 1, "###")
            print("Titulo:", lista_ocorrencias[i]["titulo"])
            print("Descrição:", lista_ocorrencias[i]["descricao"])
            print("Implicações:", lista_ocorrencias[i]["implicacoes"])
            print("Status:","sim" if lista_ocorrencias[i]["status"] == True else "não")
            print("Prazo (em dias):", lista_ocorrencias[i]["prazo"])

    else:
        print("Não existem ocorrências cadastradas.")

def listagem(ocorrencias_ativas):
    def cadastro(lista_ocorrencias):
    titulo = input("Entre com o titulo da ocorrência:")
    descricao = input("Entre com o descrição da ocorrência:")
    implicacoes = input("Entre com as implicações da ocorrência:")
    em_atividade = input ("Está em atividade? (sim|não)")
    status = True if em_atividade =="sim"else False
    prazo = int(input("Entre com a estimativa de prazo em dias:"))
    ocorrencia = dict(titulo = titulo, descricao = descricao, implicacoes = implicacoes, em_atividade = em_atividade, status = status, prazo = prazo )
    lista_ocorrencias.append(ocorrencia)
    print("Ocorrência cadastrada com sucesso!")

def listagem(lista_ocorrencias):
    tamanho = len(lista_ocorrencias)
    if tamanho > 0:
        print("---Listagem de todas as ocorrências ativas---")
        existem_ativas = False
        for i in range(tamanho):
            if lista_ocorrencias[i]["status"] == True:
                print("### Ocorrência" , i + 1, "###")
                print("Titulo:", lista_ocorrencias[i]["titulo"])
                print("Descrição:", lista_ocorrencias[i]["descricao"])
                print("Implicações:", lista_ocorrencias[i]["implicacoes"])
                print("Status:","sim" if lista_ocorrencias[i]["status"] == True else "não")
                print("Prazo (em dias):", lista_ocorrencias[i]["prazo"])
                existem_ativas = True
        if not existem_ativas = False:    
            print("Não existem ocorrências ativas")
    else:
        print("Não existem ocorrências cadastradas.")



#execução
lista_ocorrencias = []
menu_ocorrencias(lista_ocorrencias)










