def acha_maior(lista):
    local_maior = 0
    maior = lista[local_maior]
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
            local_maior = i
    return local_maior


lista = [2, 4, 76, 56, 98, 12]
indice_maior = acha_maior(lista)
print(indice_maior,lista[indice_maior])