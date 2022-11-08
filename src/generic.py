def escrever_arquivo(arquivo, string):
    #Adiciona uma string em um arquivo
    #Se o arquivo não existir, ele é criado
    with open(arquivo, 'a') as arquivo:
        arquivo.write(string)
        arquivo.close()

def lista():
    #Retorna o conteúdo de "palavras.txt"
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

def sort_segundoelemento(entrada):
    def segundo(valor):
        return valor[1]
    entrada.sort(key=segundo)
    return entrada

