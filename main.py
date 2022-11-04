from src.funcoes import comparatd

k = comparatd()
if len(k) > 1:
    print("Senhas Encontradas!\n")
    for i in range(len(k)):
        print("Usuário "+k[i][0]+" Senha: "+k[i][1])