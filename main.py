from src.generic import *
from src.encrypt import *
from src.funcoes import *

#print(senhas()[0])

#frase = input("senha")
#aha = codificar_senha(frase)
#print(aha)

#senhas_para_arquivo('k')
#print(find('JqnPIZYP5+WTMI+tIAplfXhbY0tUd82xgV+wrss7ucbHumwI5bs5epKQ7SO7v6y5c3RzHNhF+0V+ivSbRgamqA=='))

k = comparatd()
if len(k) > 1:
    print("Senhas Encontradas!\n")
    for i in range(len(k)):
        print("Usuário "+k[i][0]+" Senha: "+k[i][1])