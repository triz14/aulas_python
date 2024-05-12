# Exercicio 3
# Faça uma função que recebe uma lista de strings e retorna uma nova lista contendo apenas as strings que começa com "a"
lista = ["antes", "ontem", "amor", "legal"]

def letra_a(lista):
    lista_a = []
    for elemento in lista:
        primeira_letra = elemento[0]
        if primeira_letra == "a":
            lista_a.append(elemento)
    return lista_a

a = letra_a(lista)
print(a)