# função que acha os pares dentro de uma lista
def acha_pares(lista_numeros):
    pares = []
    for elem in lista_numeros:
        if elem%2==0:
            pares.append(elem)
    return pares

lista_2 = [32,5,31,245,75,23,542,21,32,24]
filtro_pares = acha_pares(lista_2)
print(filtro_pares)
