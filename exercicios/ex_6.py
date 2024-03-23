#Exercício 6
#Tendo como entrada a altura e o sexo (codificado da seguinte forma: 1:feminino 2:masculino) de uma pessoa, construa um programa que calcule e imprima seu peso ideal, utilizando as seguintes Fórmulas:
#- para homens: (72.7 * Altura) - 58
#- para mulheres: (62.1 * Altura) - 44.7
sexo = input("Digite seu sexo 1:feminino, 2:masculino: ")
altura = float(input("Digite sua altura: "))
imc_mulheres = (62.1*altura)-44.7
imc_homens = (72.1*altura)-58

if sexo == '1':
    print(f"Seu peso ideal é {imc_mulheres}")
else:
    print(f"Seu peso ideal é {imc_homens}")
