# Exercicio 4
# Escreva uma função que recebe uma lista de números e retorna uma nova lista contendo apenas os números pares
lista = [1,2,3,4,5,6,7,8,9,10]

def num_pares(lista):
    lista_pares = []
    for elemento in lista:
        if elemento%2 == 0:
            lista_pares.append(elemento)
    return lista_pares

a = num_pares(lista)
print(a)