from src.funcoes import (
    criptografaCombinacoes,
    combinations,
    comparatd,
    listas,
    senhas
)

senha_com_nome = listas()

senhas_ou_nomes = senhas(senha_com_nome)

listadesenhas = senhas_ou_nomes[0]
listadenomes = senhas_ou_nomes[1]

combinaciones = combinations()

combinacoes_cripto = criptografaCombinacoes(combinaciones)

comparador = comparatd(combinaciones, combinacoes_cripto, listadesenhas, listadenomes)