id = 1 # toda ocorrencia vai comecar no 1
def menu_ocorrencias(lista_ocorrencias, id):
    opcao = 1
    id = len(lista_ocorrencias) + 1
    while opcao != 0:
        print("---Menu de Ocorrências---")
        print("1 - Cadastro de ocorrência")
        print("2 - Listar todas ocorrências")
        print("3 - Listar todas ocorrências ativas")
        print("4 - Buscar ocorrências por titulo")
        print("5 - Alterar atividade da ocorrência")
        print("6 - Remover ocorrencia")
        print("7 - Editar ocorrencia")
        print("8 - Buscar Ocorrência pelo Mês")
        print("9 - Buscar ocorrência pelo palavra chave")
        print("0 - Sair")
        opcao = int(input("Entre com a opção>>"))
        if opcao == 1:
            print("---Cadastro---")
            cadastro(lista_ocorrencias, id)
            id += 1 # aqui vai estar somando com a ocorrencia anterior
        elif opcao == 2:
            print("---Listagem---")
            listagem(lista_ocorrencias)
        elif opcao == 3:
            print("Listagem[ATIVAS]")
            listagem_ativas(lista_ocorrencias)
        elif opcao == 4:
            print("Busca por titulo")
            titulo = input("Entre com o titulo da ocorrencia: ")
            posicao = buscar_ocorrencia(lista_ocorrencias, titulo)
            if posicao != -1:
                print("***Ocorrência Encontrada!***")
                impressao_ocorrencia(lista_ocorrencias[posicao],posicao)
            else:
                print("Ocorrência não encontrado!")
        elif opcao == 5:
            print("Alterar de Status de Atividade")
            titulo = input("Entre com o titulo da ocorrencia: ")
            posicao = buscar_ocorrencia(lista_ocorrencias, titulo)
            if posicao != -1:
                print("***Ocorrência Encontrada!***")
                impressao_ocorrencia(lista_ocorrencias[posicao],posicao)
                resp = input("Deseja alterar a situação da atividade ""da ocorrência? (sim|não)")
                if resp == "sim":
                    lista_ocorrencias[posicao]["status"] = not lista_ocorrencias[posicao]["status"]
                    print("Alteração feita com sucesso!")
                else:
                    print("Saindo sem alterações")
            else:
                print("Ocorrência não entrada!")
        elif opcao == 6:
            print("Remoção de ocorrência")
            titulo = input("Entre com o titulo da ocorrencia: ")
            posicao = buscar_ocorrencia(lista_ocorrencias, titulo)
            if posicao != -1:
                print("***Ocorrência Encontrada!***")
                impressao_ocorrencia(lista_ocorrencias[posicao],posicao)
                resp = input("Deseja remover a ocorrência? (sim|não)")
                if resp == "sim":
                    lista_ocorrencias.pop(posicao)
                    print("Remoção realizada com sucesso!")
                else:
                    print("Saindo sem alterações")
            else:
                print("Ocorrência não entrada!")

        elif opcao == 7:
            print("Editar a ocorrência")
            titulo = input("Entre com o titulo da ocorrencia: ")
            posicao = buscar_ocorrencia(lista_ocorrencias, titulo)
            if posicao != -1:
                print("***Ocorrência Encontrada!***")
                impressao_ocorrencia(lista_ocorrencias[posicao],posicao)
                resp = input("Deseja editar a ocorrência? (sim|não)")
                if resp == "sim":
                    editar_lista(lista_ocorrencias, posicao)
                    print("Edição realizada com sucesso!")
                else:
                    print("Saindo sem alterações")
            else:
                print("Ocorrência não entrada!")

        elif opcao == 8:
            print("Busca de ocorrência por mês referente a data inserida")
            mes = input("Insira o mês da ocorrência: ")  # pede o mês para o usuário
            ocorrencias_encontradas = busca_data(lista_ocorrencias, mes)  # chama a função busca_data para buscar as ocorrências do mês dado pelo input
            quantidade_ocorrencias = 0  # variável para contar quantas ocorrências foram encontradas
            for ocorrencia in ocorrencias_encontradas:  
                quantidade_ocorrencias += 1  # incrementa a variável de contagem
                impressao_ocorrencia(ocorrencia, lista_ocorrencias.index(ocorrencia))  # imprime as informações da ocorrência encontrada
            if quantidade_ocorrencias:
                print("Foram encontradas", quantidade_ocorrencias, "ocorrências em", mes)  # se alguma ocorrência foi encontrada, imprime a quantidade de ocorrências e o mês
            else:
                print("Não foram encontradas ocorrências neste mês.") 


        elif opcao == 9:  
            print("Busca na ocorrencia a palavra chave pelo titulo")
            titulo = input("Entre com o título da ocorrência: ")
            posicoes = palavra_chave(lista_ocorrencias, titulo)  # chama a função palavra_chave para obter as posições das ocorrências que contém a palavra-chave
            if posicoes:  # se foram encontradas ocorrências com a palavra-chave
                print("***Ocorrências encontradas!***")
                for posicao in posicoes:  # percorre a lista de posições das ocorrências encontradas
                    impressao_ocorrencia(lista_ocorrencias[posicao], posicao)  
            else:
                print("Ocorrência não encontrada!") 

            
        
        elif opcao == 0:
            print("Saindo do programa!!!")
        else:
            print("Opção Inválida!")
 
def cadastro(lista_ocorrencias, id):
    titulo = input("Entre com o título da ocorrência:")
    descricao = input("Entre com a descrição da ocorrência:")
    implicacoes = input("Entre com as implicações da ocorrência:")
    em_atividade = input("Está em atividade? (sim|não)")
    status = True if em_atividade == "sim" else False
    prazo = int(input("Entre com a estimativa de prazo em dias:"))
    data = input("Entre com a data por exemplo dd/mm/aaaa") #B
    ocorrencia = dict(id = id,titulo = titulo, 
                    descricao = descricao, 
                    implicacoes = implicacoes, 
                    status = status, prazo = prazo,
                    data = data)#B
    lista_ocorrencias.append(ocorrencia)
    print("Ocorrência cadastrada com sucesso!")
 
def listagem(lista_ocorrencias):
    tamanho = len(lista_ocorrencias)
    if tamanho > 0:
        print("---Listagem de todas as ocorrências---")
        for i in range(tamanho):
            impressao_ocorrencia(lista_ocorrencias[i], i)
            
    else:
        print("Não existem ocorrências cadastradas.")
    
def listagem_ativas(lista_ocorrencias):
    tamanho = len(lista_ocorrencias)
    if tamanho > 0:
        print("---Listagem de todas as ocorrências ativas---")
        existem_ativas = False
        for i in range(tamanho):
            if lista_ocorrencias[i]["status"] == True:
                impressao_ocorrencia(lista_ocorrencias [i], i)
                existem_ativas = True
        if not existem_ativas:
            print("Não existem ocorrências ativas")
                
    else:
        print("Não existem ocorrências cadastradas.")


def impressao_ocorrencia(ocorrencia, i):
    print("### ID",ocorrencia["id"],"###")
    print("Titulo:", ocorrencia["titulo"])
    print("Descrição:", ocorrencia["descricao"])
    print("Implicações:", ocorrencia["implicacoes"])
    print("Status:","sim" if ocorrencia["status"] == True else "não")
    print("Prazo (em dias):", ocorrencia["prazo"])
    print("data:", ocorrencia["data"])



def editar_lista (lista_ocorrencias,posicao):
    descricao = input("Entre com a descrição da ocorrência:")
    implicacoes = input("Entre com as implicações da ocorrência:")
    em_atividade = input("Está em atividade? (sim|não)")
    status = True if em_atividade == "sim" else False
    prazo = int(input("Entre com a estimativa de prazo em dias:"))
    data = input("Entre com a data por exemplo dd/mm/yyyy")
    
    lista_ocorrencias[posicao]["descricao"] = descricao
    lista_ocorrencias[posicao]["implicacoes"] = implicacoes
    lista_ocorrencias[posicao]["status"] = status
    lista_ocorrencias[posicao]["prazo"] = prazo


def buscar_ocorrencia(lista_ocorrencias, titulo):
    tamanho = len(lista_ocorrencias)
    if tamanho > 0:
        for i in range(tamanho):
            if lista_ocorrencias[i]["titulo"] == titulo:
                return i
        return -1        
    else:
        return -1


def busca_data(lista_ocorrencias, mes):
    lista_data = []  
    for ocorrencia in lista_ocorrencias:  # inseri sobre cada ocorrência na lista de ocorrências
        data = ocorrencia['data']  # atribui a variável 'data' na data da ocorrência atual
        dia, mes_, ano = data.split('/')  # usa o método split() para dividir a data em dia, mês e ano
        # agora temos 3 variáveis - 'dia', 'mes_' e 'ano' - que contêm os respectivos componentes da data da ocorrência atual
        if mes == mes_:  # verifica se o mês buscado corresponde ao mês da ocorrência atual
            lista_data.append(ocorrencia)  # adiciona a ocorrência atual à lista de ocorrências encontradas
    return lista_data  # retorna a lista de ocorrências encontradas por mês




def palavra_chave(lista_ocorrencias, titulo): #D
    lista_chave = []  
    for i in range(len(lista_ocorrencias)):  # percorre a lista de ocorrências pelo índice
        if titulo in lista_ocorrencias[i]["titulo"]:  # verifica se a palavra chave está presente no título da ocorrência
            lista_chave.append(i)  # adiciona a posição da ocorrência na lista de posições
    return lista_chave  







#execução
lista_ocorrencias = []
menu_ocorrencias(lista_ocorrencias, id)












