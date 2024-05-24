def soma_lista(lista):
    soma = 0
    for elem in lista:
        soma += elem
    return soma

def media_lista(lista):
    soma = soma_lista(lista)
    media = soma/len(lista)
    return media

lista = [1,6,9,4]
print(media_lista(lista))
