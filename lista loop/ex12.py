'''Faça um programa que calcule o mostre a média aritmética de N notas.'''

qtd_u = int(input("Digite a quantidade de números desjados: "))
qtd = 0
media = 0
soma = 0

while qtd < qtd_u:
    num = input("Digite um número: ")
    if num.isnumeric():
        num = int(num)
        qtd += 1
        soma += num
    else:
        print("Tem que ser número")
media = soma/qtd
print(media)
