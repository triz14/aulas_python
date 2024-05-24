# verifica se o elemento digitado está na lista
def verifica_elemento(lista,elem):
    for i in range(len(lista)):
        if lista[i] == elem:
            return True
    return False

def forca_opcao(msg,msg_erro,lista_opcoes):
    opcao = input(msg)
    while not verifica_elemento(lista_opcoes,opcao):
        print(msg_erro)
        opcao = input(msg)
    return opcao

carros = ['up','uno','celtinha brabo','gol']
carro = forca_opcao("Qual carro lhe interessou?\n->",'Opção inválida',carros)