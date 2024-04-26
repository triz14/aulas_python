'''Faça um programa que leia uma quantidade indeterminada de números positivos e
conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100].
A entrada de dados deverá terminar quando for lido um número negativo.'''

# 1º tentativa

intervalo1 = 0
intervalo2 = 0
intervalo3 = 0
intervalo4 = 0

while True:
    num = input("Digite um numero entre 0 a 100 e maior que 100 para sair: ")
    while not num.isnumeric():
        num = input("Digite um numero entre 0 a 100 e maior que 100 para sair: ")
    num = int(num)
    if num <= 25:
        intervalo1 += 1
    elif num <= 50:
        intervalo2 += 1
    elif num <= 75:
        intervalo3 += 1
    elif num <= 100:
        intervalo4 += 1
    else:
        break