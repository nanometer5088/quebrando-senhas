def senhas_para_arquivo(senha):
    with open('senhas_quebradas.txt', 'a') as arquivo:
        arquivo.write(senha+'\n')
        arquivo.close()

def escrever_arquivo(arquivo, string):
    with open(arquivo, 'a') as arquivo:
        arquivo.write(string)
        arquivo.close()

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