#Exercício 9
#Escreva um programa para ler 3 valores inteiros e escrever o maior deles. Considere que o usuário não informará valores iguais.
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite mais um número: "))

if n1 > n2 and n1 > n3:
    print(f"O maior número é {n1}")
elif n2 > n1 and n2 > n3:
    print(f"O maior número é {n2}")
else:
    print(f"O maior número é {n3}")
