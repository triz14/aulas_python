'''Faça um programa que receba dois números inteiros e gere os números inteiros
que estão no intervalo compreendido por eles'''

# 1º tentativa

'''n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

while n2<n1:
	print("Números inválidos")
	n1 = int(input("Digite o primeiro número: "))
	n2 = int(input("Digite o segundo número: "))
else:
	for i in range(n1, n2, 1):
		print(i)'''

# 2º tentativa

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

if n2 < n1:
    aux = n1
    n1 = n2
    n2 = aux

while n1 <= n2:
    print(n1)
    n1 += 1

