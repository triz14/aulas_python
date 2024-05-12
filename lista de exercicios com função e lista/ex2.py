# Exercicio 2
# Crie uma função que recebe uma lista de números e retorna o maior elemento da lista
lista = [2,3,4,8,6]

def maior_num(lista):
    maior = lista[0]
    for elemento in lista:
        if elemento > maior:
            maior = elemento
    return maior

a = maior_num(lista)
print(a)