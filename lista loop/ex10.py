# Exercicio 10
num = int(input("Digite um numero: "))
i = num - 1
while i > 0:
    num *= i
    i -= 1
    print(num)