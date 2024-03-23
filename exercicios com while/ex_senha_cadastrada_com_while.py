senha_cadastrada = '1234'
senha = input("Diga sua senha: ")
qtd = 1
while senha != senha_cadastrada and qtd < 3:
    print(f"Vc é hacker? Só mais {3 - qtd} tentativas")
    senha = input("Diga sua senha: ")
    qtd += 1
if senha == senha_cadastrada:
    print("Acesso liberado!")
else:
    print("Sai hacker!!!")