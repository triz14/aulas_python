# Exercicio 9
# Escreva uma função que recebe uma lista de números e retorna a média aritmética dos elementos da lista
lista = [2,2,2,2,2]

def media(lista):
    soma = 0
    media = 0
    for elemento in lista:
        soma += elemento
    media = soma / len(lista)
    return media

a = media(lista)
print(a)

