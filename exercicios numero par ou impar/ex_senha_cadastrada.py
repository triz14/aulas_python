tentativas = 1
senha_cadastrada = '1234'
senha = input("Diga sua senha: ")
while senha != senha_cadastrada and tentativas < 3:
    print("Vc é hacker? ")
    senha = input("Diga sua senha: ")
    tentativas += 1
if senha == senha_cadastrada:
    print("Acesso liberado")
else:
    print("Sai hacker")