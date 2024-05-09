#1 - Declare uma lista com 10 numeros. Faça a soma e a media dos
#numeros loopando nela.
lista = [4,3,1,0,2,3,10,1,11,98]
soma = 0
for num in lista:
    soma += num
print(soma,soma/len(lista))

# Outra forma de fazer
soma = 0
for i in range(len(lista)):
    soma += lista[i]
print(soma,soma/len(lista))