# Minha resolução
print("Seja bem vindo")

ano_nasc = int(input("Digite o ano em que você nasceu: "))

if ano_nasc >= 2007:
    print("Não é permitida a enda de bebidas alcoolicas")
else:
    end = input("Digite seu endereço: ")
    vinho = int(input(
        "Escolha seus vinhos opções: digite 1 para Merlot de merda R$70 , 2 para Nerdola R$90 e 3 para Barbie R$110 digite uma das opções: "))

    if vinho == 1:
        qt = int(input("Quantas garrafas você deseja comprar? "))
        preco = 70
        preco_t = qt * preco
    elif vinho == 2:
        qt = int(input("Quantas garrafas você deseja comprar? "))
        preco = 90
        preco_t = qt * preco
    else:
        qt = int(input("Quantas garrafas você deseja comprar? "))
        preco = 110
        preco_t = qt * preco

    if preco_t > 100:
        print("Frete grátis")
        total = preco_t
    else:
        total = preco_t + 20
    print(f"Obrigado pela compra o valor total é ${total}")

# Resolução do professor

vinho1 = 'Chapinha'
vinho2 = 'Cantinho do Vale'
vinho3 = 'Sangue de Boi'
preco1 = 10
preco2 = 20
preco3 = 30
frete = 10
print("Seja bem vindo à vinheria agnello!!!!!!!")
ano = int(input("Diga seu ano de nascimento: "))
idade = 2024 - ano
if idade < 18:
    print("Que feio!!!! Vc não pode beber!!!")
else:
    endereco = input("Diga seu endereço: ")
    opcao = input(f"Temos os vinhos:\n{vinho1} : R${preco1:.2f}"
                  f"\n{vinho2} : R${preco2:.2f}"
                  f"\n{vinho3} : R${preco3:.2f}.\n Qual você quer? ")
    if opcao == vinho1:
        preco = preco1
    elif opcao == vinho2:
        preco = preco2
    else:
        preco = preco3
    qtd = int(input(f"Diga qts garrafas de {opcao}: "))
    valor = qtd*preco
    if valor > 100:
        print("Frete grátis!")
    else:
        valor += frete
    print(f"Obrigado por comprar na vinheira agnello. Vc levou {qtd}"
          f" garrafas de {opcao} por R${valor:.2f} e será entregue em "
          f"{endereco}")