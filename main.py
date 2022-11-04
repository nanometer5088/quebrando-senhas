from src.init import inicio
from src.constants import WARNING
from src.funcoes import (
    criptografaCombinacoes,
    combinations,
    comparatd,
    listas,
    senhas
)
def programa():
    senha_com_nome = listas()

    senhas_ou_nomes = senhas(senha_com_nome)

    listadesenhas = senhas_ou_nomes[0]
    listadenomes = senhas_ou_nomes[1]

    combinaciones = combinations()

    combinacoes_cripto = criptografaCombinacoes(combinaciones)

    comparador = comparatd(combinaciones, combinacoes_cripto, listadesenhas, listadenomes)

def main():
    x = inicio()
    if x == "instalado":
        print(WARNING["librariesinstalled"])
        return None
    programa()

main()