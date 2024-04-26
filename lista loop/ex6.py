'''Faça um programa que leia um nome de usuário e a sua senha e não aceite a
senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a
pedir as informações.'''

# 1º tentativa

'''# Exercicio 6
nome = input("Digite seu nome: ")
senha = input("Digite sua senha: ")

while senha == nome:
    print("A senha não pode ser igual a nome")
    senha = input("Digite sua senha: ")'''

# 2º tentativa

usuario = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

while senha == usuario:
    print("A senha não pode ser igual o usuário")
    usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")
print("senha aceita")
