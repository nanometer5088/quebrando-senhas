def listas():
    i = 0
    vazio = ''
    arquivo = open('usuarios_senhascodificadas.txt', 'r', encoding='utf-8')
    linhas = arquivo.readlines()
    tamanho = len(linhas)
    arquivo.close()
    vet = [0] * tamanho
    arquivo = open('usuarios_senhascodificadas.txt', 'r', encoding='utf-8')
    while True:
        lelinha = arquivo.readline().rstrip()
        if lelinha == vazio:
            break
        vet[i] = lelinha.split(':')
        i += 1
    arquivo.close()
    return vet

def senhas():
    senha_com_nome = listas('usuarios_senhascodificadas.txt')
    listadesenhas = []
    listadenomes = []
    for i in range(len(senha_com_nome)):
        listadesenhas.append(senha_com_nome[i][1])
    for i in range(len(senha_com_nome)):
        listadenomes.append(senha_com_nome[i][0])
    return listadesenhas, listadenomes

def find(senha_criptografada):
    senha = senhas()[0]
    for i in range(len(senha)):
        if senha_criptografada == senha[i]:
            return senhas()[1][i]

def combinations():
    from src.generic import escrever_arquivo
    def lista():
        i = 0
        vazio = ''
        arquivo = open('palavras.txt', 'r', encoding='utf-8')
        linhas = arquivo.readlines()
        tamanho = len(linhas)
        arquivo.close()
        vet = [0] * tamanho
        arquivo = open('palavras.txt', 'r', encoding='utf-8')
        while True:
            lelinha = arquivo.readline().rstrip()
            if lelinha == vazio:
                break
            vet[i] = lelinha
            i += 1
        arquivo.close()
        return vet

    from itertools import product
    listafinal = []
    lista = lista()

    lista1 = list(product(lista, repeat=1))
    lista2 = list(product(lista, repeat=2))
    lista3 = list(product(lista, repeat=3))
    lista4 = list(product(lista, repeat=4))
    lista5 = list(product(lista, repeat=5))
    listatotal = lista1 + lista2 + lista3 + lista4 + lista5

    for i in range(len(listatotal)):
        if len(listatotal[i]) == 1:
            listafinal.append(listatotal[i][0])

        elif len(listatotal[i]) == 2:
            listafinal.append(listatotal[i][0]+' '+listatotal[i][1])

        elif len(listatotal[i]) == 3:
            listafinal.append(listatotal[i][0]+' '+listatotal[i][1]+' '+listatotal[i][2])

        elif len(listatotal[i]) == 4:
            listafinal.append(listatotal[i][0]+' '+listatotal[i][1]+' '+listatotal[i][2]+' '+listatotal[i][3])

        elif len(listatotal[i]) == 5:
            listafinal.append(listatotal[i][0]+' '+listatotal[i][1]+' '+listatotal[i][2]+' '+listatotal[i][3]+' '+listatotal[i][4])

    for i in range(len(listafinal)):
        escrever_arquivo('arquivograndeprakaralho', listafinal[i])
        escrever_arquivo('arquivograndeprakaralho', '\n')
    return listafinal