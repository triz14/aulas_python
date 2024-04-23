'''Faça um programa que leia 5 números e informe a soma e a média dos números.'''

# while True:
#     n1 = int(input("Digite o primeiro número: "))
#     n2 = int(input("Digite o segundo número: "))
#     n3 = int(input("Digite o terceiro número: "))
#     n4 = int(input("Digite o quarto número: "))
#     n5 = int(input("Digite o quinto número: "))
#     soma = n1+n2+n3+n4+n5
#     media = (n1+n2+n3+n4+n5)/5
#     print(f"A soma de numero é {soma} e a média dos numeros é {media}")
#     break


qtd = 0 
soma = 0

while qtd < 5:
    num = input("Digite um número: ")
    if num.isnumeric():
        num = int(num)
        qtd += 1
        soma += num
        media = (soma)/qtd
    else:
        print("Tem que ser número")
print(f"A soma dos números é {soma} e a média é {media}")
