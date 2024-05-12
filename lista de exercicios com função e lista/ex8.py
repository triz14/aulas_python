# Exercicio 8
# Crie uma função que recebe uma lista de números e retorna uma nova lista com os elementos em ordem inversa
lista = [10,20,30,40]

def inverso(lista):
    lista_inversa = []
    for i in range(len(lista) -1, -1, -1):
        lista_inversa.append(lista[i])
    return lista_inversa

a = inverso(lista)
print(a)