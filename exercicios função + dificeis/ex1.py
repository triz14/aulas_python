# função que verfica se é um número
def verifica_numero(msg,msg_erro):
    num = input(msg)
    while not num.isnumeric():
        print(msg_erro)
        num = input(msg)
    num = int(num)
    return num

print(verifica_numero("Digite um numero: ", "é numero"))