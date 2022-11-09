from os import system, remove
from src.constants import WARNING, INTRO

def inicio():
    #Início do programa e indrodução para o usuário
    system("cls || clear")
    input(INTRO["mainintro"])

    #Verifica a existência dos arquivos gerados pelo
    #programa, e remove-os caso os mesmos existam
    #'senhas_quebradas.txt' e 'senhas_nao_quebradas.txt'
    try:
        remove('senhas_quebradas.txt')
    except OSError:
        pass
    
    try:
        remove('senhas_nao_quebradas.txt')
    except OSError:
        pass

    # Detecção e instalação das dependências - Caso não estejam instaladas,
    # a instalação ocorre e o programa é encerrado. O usuário é avisado para reiniciar
    # o programa ao finalizar
    try:
        from rich.progress import track
        system("cls || clear")
    except ModuleNotFoundError:
        system("cls || clear")
        input(WARNING["libraries"])
        system("pip install -r requirements.txt --user")
        system("cls || clear")
        return "instalado"

    # Verifica por atualizações, e avisa o usuário caso encontre alguma
    try:
        import requests
        data = requests.get("https://raw.githubusercontent.com/nanometer5088/quebrando-senhas/main/VERSION")
        version = open('VERSION', 'r', encoding='utf=8')
        if version.readline().rstrip() < (data.text):
            system("cls || clear")
            input(WARNING["newversion"])
        version.close()
    except requests.exceptions.ConnectionError:
        pass