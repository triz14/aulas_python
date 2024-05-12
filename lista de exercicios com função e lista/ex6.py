# Exercicio 6
# Faça uma função que recebe duas listas e retorna uma lista contendo os elementos comuns entre as duas listas
lista_1 = [2,3,4,5,6,7,8]
lista_2 = [3,5,7,1,10,11]

def elementos_comuns(lista_1, lista_2):
    lista_comum = []
    for elemento in lista_1:
        for elemento_2 in lista_2:
            if elemento == elemento_2:
                lista_comum.append(elemento)
                break
    return lista_comum

a = elementos_comuns(lista_1, lista_2)
print(a)