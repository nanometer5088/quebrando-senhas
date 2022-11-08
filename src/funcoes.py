from src.generic import escrever_arquivo, sort_segundoelemento
from itertools import product
from os import system as sys


def listas():
    #Retorna o conteúdo de "usuarios_senhascodificadas.txt"
    #em duas listas, separados por usuário e senha
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

def senhas(senha_com_nome):
    #Retorna duas listas separadas
    #provenientes do listas()
    listadesenhas = []
    listadenomes = []
    for i in range(len(senha_com_nome)):
        listadesenhas.append(senha_com_nome[i][1])
    for i in range(len(senha_com_nome)):
        listadenomes.append(senha_com_nome[i][0])
    return listadesenhas, listadenomes

def combinations():
    #Gera todas as combinações de palavras possíveis
    #com as palavras do arquivo "palavras.txt"
    from rich.progress import track
    from src.generic import lista
    lista = lista()
    listafinal = []
    
    lista1 = list(product(lista, repeat=1))
    lista2 = list(product(lista, repeat=2))
    lista3 = list(product(lista, repeat=3))
    lista4 = list(product(lista, repeat=4))
    lista5 = list(product(lista, repeat=5))
    listatotal = lista1 + lista2 + lista3 + lista4 + lista5

    for i in track(range(len(listatotal)), "Computando as combinações..."):
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

    return listafinal

def criptografaCombinacoes(combinacoes):
    #Criptografa todas as combinações geradas
    #pela função combinations()
    from rich.progress import track
    from src.encrypt import codificar_senha
    senhascodificadas = []
    for i in track(range(len(combinacoes)), "Criptografando as combinações..."):
        senhascodificadas.append(codificar_senha(combinacoes[i]))
    return senhascodificadas

def comparatd(muchograndelistadepossibilidades, senhasgeradas, senhasdoarquivo, listadenomes):
    from rich.progress import track
    listaresultados = []
    listaparaescrever = []
    #Compara a senha criptografada com as existentes
    #no arquivo "usuarios_senhascodificadas.txt";
    #Se existir, escreve no arquivo "senhas_quebradas.txt"
    #o nome do usuário e a senha descriptografada
    def testapredefinido(senha, pos):
        for i in range(len(senhasdoarquivo)):
            if senhasdoarquivo[i] == senha:
                listaresultados.append(listadenomes[i])
                listaparaescrever.append([listadenomes[i],muchograndelistadepossibilidades[pos]])
    
    for i in track(range(len(senhasgeradas)), "Comparando as combinações criptografadas com a dos usuários..."):
        testapredefinido(senhasgeradas[i], i)

    lista1 = []
    lista2 = []
    lista3 = []
    lista4 = []
    lista5 = []
    for i in range(len(listaparaescrever)):
        if len(listaparaescrever[i][1].split()) == 1:
            lista1.append(listaparaescrever[i])

    for i in range(len(listaparaescrever)):
        if len(listaparaescrever[i][1].split()) == 2:
            lista2.append(listaparaescrever[i])
    
    for i in range(len(listaparaescrever)):
        if len(listaparaescrever[i][1].split()) == 3:
            lista3.append(listaparaescrever[i])

    for i in range(len(listaparaescrever)):
        if len(listaparaescrever[i][1].split()) == 4:
            lista4.append(listaparaescrever[i])

    for i in range(len(listaparaescrever)):
        if len(listaparaescrever[i][1].split()) == 5:
            lista5.append(listaparaescrever[i])

    sort_segundoelemento(lista1)
    for i in range(len(lista1)):
        escrever_arquivo('senhas_quebradas.txt', lista1[i][0]+':'+lista1[i][1]+'\n')
    
    sort_segundoelemento(lista2)
    for i in range(len(lista2)):
        escrever_arquivo('senhas_quebradas.txt', lista2[i][0]+':'+lista2[i][1]+'\n')

    sort_segundoelemento(lista3)
    for i in range(len(lista3)):
        escrever_arquivo('senhas_quebradas.txt', lista3[i][0]+':'+lista3[i][1]+'\n')

    sort_segundoelemento(lista4)
    for i in range(len(lista4)):
        escrever_arquivo('senhas_quebradas.txt', lista4[i][0]+':'+lista4[i][1]+'\n')

    sort_segundoelemento(lista5)
    for i in range(len(lista5)):
        escrever_arquivo('senhas_quebradas.txt', lista5[i][0]+':'+lista5[i][1]+'\n')


    x = set(listadenomes) - set(listaresultados)

    if len(listaresultados) < 1:
        sys("cls || clear")
        print("\tNenhuma senha pode ser descoberta. Insira palavras no arquivo 'usuarios_senhascodificadas.txt'")
    elif len(listaresultados) >= 1:
        print(f'\n\tSucesso!\n\n\t{len(listaresultados)} senha(s) foram descoberta(s). Essas informações foram salvas em "senhas_quebradas.txt"')
    
    #Determina se houve senhas não encontradas, e
    #insere as mesmas no arquivo "senhas_nao_quebradas.txt"
    if len(x) < 1:
        return None

    listafinal = []
    for i in range(len(x)):
        listafinal.append(listadenomes[listadenomes.index(list(x)[i])]+':'+senhasdoarquivo[listadenomes.index(list(x)[i])])
    listafinal.sort()
    for i in range(len(listafinal)):
        escrever_arquivo('senhas_nao_quebradas.txt', listafinal[i]+'\n')
    
    print(f"\t{len(x)} senha(s) não puderam ser descobertas com a wordlist dada. As senhas criptografadas estão em 'senhas_nao_quebradas.txt'")
    