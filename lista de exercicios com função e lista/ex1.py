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