# Exercicio 9
qtd = 0
qtd_pares = 0
while qtd < 10:
    num = int(input("Digite um numnero inteiro: "))
    if num%2 == 0:
        qtd_pares += 1
    qtd += 1
print(f" pares = {qtd_pares} impares = {10-qtd_pares}")