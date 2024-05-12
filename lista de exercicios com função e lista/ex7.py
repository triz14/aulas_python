# Exercicio 7
# Escreva uma função que recebe uma lista de números e retorna True se a lista estiver em ordem crescente e False caso contrário
lista = [2,1]

def crescente(lista):
    primeiro = lista[0]
    for elemento in lista:
        if primeiro > elemento:
            return False
    return True

a = crescente(lista)
print(a)