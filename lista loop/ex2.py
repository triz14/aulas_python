'''Faça um programa que leia e valide as seguintes informações:
a. Nome: maior que 3 caracteres;
b. Idade: entre 0 e 150;
c. Salário: maior que zero;
d. Sexo: 'f' ou 'm';
e. Estado Civil: 's', 'c', 'v', 'd';'''

# 1º tentativa

'''while True:
    nome = input("Digite seu nome: ")
    if len(nome) > 3:
        break
    else:
        print("Você digitou um nome com menos ou de 3 caracteres")

while True:
    idade = int(input("Digite a sua idade: "))
    if idade >= 0 and idade <=150:
        break
    else:
        print("Idade inválida")

while True:
    salario = int(input("Digite seu salário: "))
    if salario > 0:
        break
    else:
        print("Seu salário precisa ser maior que 0")

while True:
    sexo = input("Digite seu sexo: f para feminino e m para masculino: ")
    if sexo == "f" or sexo == "m":
        break
    else:
        print("Sexo Inválido")

while True:
    estado_civil = input("Digite seu estado civil: s, c, v ,d:  ")
    if estado_civil == "s" or estado_civil == "c" or estado_civil == "v" or estado_civil == "d":
        break
    else:
        print("Estado civil inválido")'''

# 2º tentativa

while True:
    nome = input("Digite seu nome: ")
    if len(nome) <= 3:
        print("Tem quer ter mais de 3 caracteres")
    else:
        break

while True:
    idade = input("Digite sua idade: ")
    if idade.isnumeric():
        idade = int(idade)
        if idade < 150:
            break
        else: 
            print("Você é imortal?")
    else:
        print("Tem que ser número")

while True:
    salario = input("Digite seu saário: ")
    if salario.isnumeric():
        salario = int(salario)
        break
    else:
        print("É número")

while True:
    sexo = input("Digite seu sexo: f ou m: ")
    if sexo == "f" or sexo == "m":
        break
    else:
        print("Digite um sexo válido")

while True:
    estado_civil = input("Digite seu estado civil: s, c, d, v: ")
    if estado_civil == "s" or estado_civil == "c" or estado_civil == "d" or estado_civil == "v":
        break
    else:
        print("Digite um estado civil válido")
