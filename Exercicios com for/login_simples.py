senha_cadastrada = '1234'
for i in range(3):
    senha = input("Diga sua senha: ")
    if senha == senha_cadastrada:
        print("Acesso Liberado!")
        break
    print(f"Sai Hacker!!!!!! Só mais {2-i} tentativas!")
if senha != senha_cadastrada:
    print("Sai Hacker")