# Exercicio 6
nome = input("Digite seu nome: ")
senha = input("Digite sua senha: ")

while senha == nome:
    print("A senha não pode ser igual a nome")
    senha = input("Digite sua senha: ")