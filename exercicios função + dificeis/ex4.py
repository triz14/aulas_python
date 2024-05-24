def meu_reverse(lista):
    for i in range(len(lista)//2):
        ultimo = len(lista) - 1
        aux = lista[i]
        lista[i] = lista[ultimo - i]
        lista[ultimo - i] = aux
    return lista

lista = [1,2,3,4,5,6,7,8,9]
lista2 = lista[:]
meu_reverse(lista2)
print(lista2)
print(lista)