#Exercício 4
#As maçãs custam R$ 0,30 cada se forem compradas menos do que uma dúzia, e R$ 0,25 se forem compradas pelo menos doze. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o valor total da compra.
num_macas = int(input("Digite o numero de maçãs compradas: "))

if num_macas >= 12:
    print(f"O valor total da compra é de {num_macas*0.25}")
else:
    print(f"O valor total da compra é de {num_macas*0.30}")