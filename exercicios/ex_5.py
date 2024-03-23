#Exercício 5
#Escreva um programa para ler 3 valores inteiros (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.

val1 = int(input("Digite o primeiro valor: "))
val2 = int(input("Digite o segundo valor: "))
val3 = int(input("Digite o terceiro valor: "))

a = val1
b = val2
c = val3

# Comparando e ordenando os valores
if a > b:
    aux = b
    b = a
    a = aux
    # agora sei que a é menor que b

if b > c:
    aux = c
    c = b
    b = aux
    # agora b é menor que c

if a > b:
    aux = b
    b = a
    a = aux
    # garantindo que a é menor que b

if a > c:
    aux = c
    c = a
    a = aux
    # garantindo que a é o menor número

print("Os valores em ordem crescente são:", a, b, c)
