while True:
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
        print("Estado civil inválido")