# Exercicio 1
# Escreva uma função que recebe uma lista de númeeros e retorna a soma de todos os elementos da lista
lista = [2,2,2,2,2]

def soma(lista):
    soma = 0
    for elemento in lista:
        soma += elemento
    return soma

a = soma(lista)
print(a)


def somar(lista_da_funcao):
    soma = 0
    for elem in lista_da_funcao:
        soma += elem
    return soma

lista = [2,2,2,2,2]
print(somar(lista))

def maior_num(lista_da_func):
    local_maior = 0
    maior = lista[local_maior]
    for i in range(len(lista_da_func)):
        if lista[i] > maior:
            maior = lista[i]
            local_maior = i
    return local_maior

lista = [1,2,3,4,5,6,7,8,9,10]
print(maior_num(lista))
