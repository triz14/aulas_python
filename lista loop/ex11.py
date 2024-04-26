'''Faça um programa que peça um número inteiro e determine se ele é ou não um
número primo. Um número primo é aquele que é divisível somente por ele mesmo e por
1.'''

# 1º tentativa

num = int(input("Digite um número: "))
i = 2

while i < num**0.5:
    print(f"{num}%{i} = {num%i}")
    if num%2 == 0:
        print("Não é primo")
        break
    i += 1
    if num%i == 0:
        print("Não é primo")
        break
if i >= num**0.5:
    print("é primo")

