# Minha resolução
print("Seja bem vindo!")

while True:
    ano = input("Digite o ano em que você nasceu: ")

    if not ano.isnumeric():
        print("Valor inválido")
    else:
        ano = int(ano)
        idade = 2024 - ano
        if idade < 18:
            print("Você não pode entrar nesse site")
            break
        else:
            vinho_1 = "merlot"
            vinho_2 = "neugbauer"
            vinho_3 = "danilo"

            vinho = input(f"Escolha sua opção de vinho: digite {vinho_1} R$70,  {vinho_2} R$90 ou {vinho_3} R$110: ")

            while vinho != vinho_1 and vinho != vinho_2 and vinho != vinho_3:
                print("valor de vinho inválido")
                vinho = input(f"Escolha sua opção de vinho: digite {vinho_1} R$70,  {vinho_2} R$90 ou {vinho_3} R$110: ")
                if vinho == vinho_1 or vinho == vinho_2 or vinho == vinho_3:
                    if vinho == vinho_1:
                        preco = 70
                    elif vinho == vinho_2:
                        preco = 90
                    else:
                        preco = 110

                    qtd = input("Digite a quantidade de garrafas desejadas: ")
                    while not qtd.isnumeric():
                            print("Quantidade inválida")
                            qtd = input("Digite a quantidade de garrafas desejadas: ")
                    if qtd.isnumeric():
                        qtd = int(qtd)
                        valor_t = preco
                        frete = 0
                        if valor_t > 500:
                            print(f"O valor total da sua compra é {valor_t} e seu frete é grátis")
                        else:
                            frete = 20
                            print(f"O valor total da sua compra é {valor_t} e seu frete é {frete} totalizando {valor_t+frete}")
                            print("Obrigado pela compra")


# Resolução prof
vinho1 = 'Chapinha'
preco1 = 10
qtd1 = 0
vinho2 = 'Sangue de Boi'
preco2 = 20
qtd2 = 0
vinho3 = 'Catuaba'
preco3 = 30
qtd3 = 0
valor = 0
frete = 10
print("Seja bem vindo à vinheria Agnello!!!!!!!!!")
ano = input("Diga seu ano de nascimento: ")
while not ano.isnumeric():
    ano = input("Diga seu ano de nascimento: ")
ano = int(ano)
idade = 2024 - ano
if idade >= 18:
    endereco = input("Diga seu endereço: ")
    while True:
        opcao = input(f"Qual vinho voce quer ?\n {vinho1} : {preco1}"
                      f"\n{vinho2} : {preco2}\n{vinho3} : {preco3}")
        while opcao != vinho1 and opcao != vinho2 and opcao != vinho3:
            print("Opção inválida!")
            opcao = input(f"Qual vinho voce quer ?\n {vinho1} : {preco1}"
                      f"\n{vinho2} : {preco2}\n{vinho3} : {preco3}")

        qtd = input(f"Qtos vinhos {opcao} ?")
        while not qtd.isnumeric():
            print("Deve ser um numero!")
            qtd = input(f"Qtos vinhos {opcao} ?")
        qtd = int(qtd)

        if opcao == vinho1:
            preco = qtd * preco1
            qtd1 += qtd
        elif opcao == vinho2:
            preco = qtd * preco2
            qtd2 += qtd
        else:
            preco = qtd*preco3
            qtd3 += qtd
        valor += preco
        resposta = input("Você quer comprar mais vinhos? (s/n)\n->")
        while not (resposta == 's' or resposta == 'n'):
            print("Opção inválida!")
            resposta = input("Você quer comprar mais vinhos? (s/n)\n->")
        if resposta == 'n':
            break
    if valor >= 500:
        print("Frete Grátis")
    else:
        valor += frete
    print(f"Obrigado por comprar aqui!!!!\n"
          f"Você comprou:\n{qtd1} de {vinho1}\n{qtd2} de {vinho2}\n"
          f"{qtd3} de {vinho3} por R${valor:.2f} e"
          f" será entregue em {endereco}")
else:
    print("Sai kids")