#Exercício 5
#Escreva um programa para ler 3 valores inteiros (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.

# Solicita ao usuário que insira três números inteiros distintos
val1 = int(input("Digite o primeiro valor inteiro: "))
val2 = int(input("Digite o segundo valor inteiro: "))
val3 = int(input("Digite o terceiro valor inteiro: "))

# Inicializa as variáveis com os valores fornecidos pelo usuário
a = val1
b = val2
c = val3
# Ordenação
if a > b:
    aux = a
    a = b
    b = aux

if a > c:
    aux = a
    a = c
    c = aux

if b > c:
    aux = b
    b = c
    c = aux

# Mostra os valores ordenados
print("Os valores em ordem crescente são:", a, b, c)

# outra forma (pior)
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

#outra forma de fazer o exercicio

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
n3 = int(input("Digite o terceiro valor: "))

if n1 == n2 or n2 == n3 or n1 == n3:
    print("Não será lido valores iguais")

menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

maior = n1
if n2> n1:
    maior = n2
if n3> n2:
    maior = n3

meio = (n1+n2+n3) - menor - maior
print(n1, n2, n3)