#Exericcio para calcular o imposto de renda de caordo com o salário informado
salario = float(input("Digite seu salário: "))

if salario <= 1903.98:
    print("Você está isento do imposto de renda")
elif salario <= 2836.65:
    print(f"Seu desconto de imposto de renda é de 7,5%, seu salário é {salario - salario * 0.75}")
elif salario <= 3751.05:
    print(f"Seu desconto de imposto de renda é de 15%, seu salário é {salario - salario * 0.15}")
elif salario <= 4664.68:
    print(f"Seu desconto de imposto de renda é de 22,5%, seu salário é {salario - salario * 0.225}")
else:
    print(f"Seu desconto de imposto de renda é de 27,5%, seu salário é {salario - salario * 0.275}")