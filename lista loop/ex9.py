'''Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de
números pares e a quantidade de números ímpares.'''

# 1º tentativa

'''qtd = 0
qtd_pares = 0
while qtd < 10:
    num = int(input("Digite um numnero inteiro: "))
    if num%2 == 0:
        qtd_pares += 1
    qtd += 1
print(f" pares = {qtd_pares} impares = {10-qtd_pares}")'''

# 2º tentativa

num = input("Digite um  número: ")
qtd = 1
pares = 0

while qtd < 10:
    num = input("Digite um  número: ")
    if num.isnumeric():
        num = int(num)
        if num%2 == 0:
            pares += 1
        qtd += 1
    else:
        print("Tem que ser número")
print(f"A quantidade de pares é {pares} e a de impares é {qtd - pares}")