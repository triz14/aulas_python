#Exercício 2
#Escreva um programa para ler o ano de nascimento de uma pessoa e escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que ela nasceu).
ano = int(input("Digite o ano que você nasceu: "))

if ano <= 2008:
    print("Você pode votar esse ano!!")
else:
    print("Desculpe, você não pode votar esse ano")
