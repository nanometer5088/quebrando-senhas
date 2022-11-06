from os import system as sys
from src.constants import WARNING, INTRO

def inicio():
    #Início do programa e indrodução para o usuário
    sys("cls || clear")
    input(INTRO["mainintro"])

    # Verifica por atualizações, e avisa o usuário caso encontre alguma
    try:
        import requests
        data = requests.get("https://raw.githubusercontent.com/nanometer5088/quebrando-senhas/main/VERSION")
        version = open('VERSION', 'r', encoding='utf=8')
        if version.readline().rstrip() < (data.text):
            sys("cls || clear")
            input(WARNING["newversion"])
        version.close()
    except requests.exceptions.ConnectionError:
        pass

    # Detecção e instalação das dependências - Caso não estejam instaladas,
    # a instalação ocorre e o programa é encerrado. O usuário é avisado para reiniciar
    # o programa ao finalizar
    try:
        from rich.progress import track
        sys("cls || clear")
    except ModuleNotFoundError:
        sys("cls || clear")
        input(WARNING["libraries"])
        sys("pip install -r requirements.txt --user")
        sys("cls || clear")
        return "instalado"