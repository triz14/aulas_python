'''Faça um programa que calcule o fatorial de um número inteiro fornecido pelo
usuário. Ex.: 5!=5.4.3.2.1=120'''

# # Exercicio 10
# num = int(input("Digite um numero: "))
# i = num - 1
# while i > 0:
#     num *= i
#     i -= 1
#     print(num)

num = int(input("Digite um número: "))
i = num - 1

while i > 0:
    num *= i
    i -= 1
    print(num)