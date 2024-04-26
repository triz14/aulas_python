'''A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... Faça um
programa capaz de gerar a série até o n−ésimo termo.'''

# 1º tentativa

'''num = int(input("Digite um numero: "))
a = 1
b = 1
i = 2
while i < num:
    c = a + b
    a = b
    b = c
    print(c)
    i += 1'''

# 2º tentativa

num = input("Digite um número: ")

a = 1
b = 1
i = 2

while i < num:
    c = a + b
    a = b
    b = c
    print(c)
    i += 1