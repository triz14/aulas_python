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
