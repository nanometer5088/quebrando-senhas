def senhas_para_arquivo(senha):
    with open('senhas_quebradas.txt', 'a') as arquivo:
        arquivo.write(senha+'\n')
        arquivo.close()

def escrever_arquivo(arquivo, string):
    with open(arquivo, 'a') as arquivo:
        arquivo.write(string)
        arquivo.close()