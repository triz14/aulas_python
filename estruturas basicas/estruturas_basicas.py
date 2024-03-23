#Estruturas básicas do phyton
frase = "Hello world!"
primeiro_numero = 1
segundo_numero = 1.5
booleana = False
print(frase)
print(type(frase))
print(primeiro_numero)
print(type(primeiro_numero))
print(segundo_numero)
print(type(segundo_numero))
print(booleana)
print(type(booleana))

#Mini-calculadora em phyton
nome = input(("Digite seu nome: "))

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))

soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2

print(f"Seja bem vindo {nome}")
print(f"A soma entre {n1} e {n2} é {soma}")
print(f"A subtração entre {n1} e {n2} é {sub}")
print(f"A multiplicação entre {n1} e {n2} é {mult}")
print(f"A divisão entre {n1} e {n2} é {div}")

#Valores podem ser reatribuídos ou somados nas variáveis já existentes
nome = input(("Digite seu nome: "))
frase = "Eu"
frase = frase + " me"
frase = frase + " chamo "
frase = frase + nome

print(frase)

a = 3
b = 5
#Aux guarda um valor (geralmente de uma variável)
aux = a

a = b
b = aux

print(a)
print(b)