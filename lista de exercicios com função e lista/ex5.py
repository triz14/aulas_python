# Exercicio 5
# Crie uma função que recebe uma lista de palavras de retorna o número de letras de cada palavra em uma nova lista
lista = ["amor", "ontem", "amanha", "bia"]

def contador(lista):
    lista_num = []
    for elemento in lista:
        num = len(elemento)
        lista_num.append(num)
    return lista_num

a = contador(lista)
print(a)