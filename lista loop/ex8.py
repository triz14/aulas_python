# Exercicio 8
num = int(input("Digite um numero: "))
a = 1
b = 1
i = 2
while i < num:
    c = a + b
    a = b
    b = c
    print(c)
    i += 1