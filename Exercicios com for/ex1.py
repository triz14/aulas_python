# peça 10 numeros ao usuario e conte a qtd de numeros pares e numeros impares
pares = 0
impares = 0

for i in range(10):
    num = input("Digite um número: ")
    while not num.isnumeric():
        print("Valor inválido")
        num = input("Digite um número: ")
    num = int(num)
    if num%2 == 0:
        pares += 1
    else:
        impares += 1
print(f"A quantidade de pares é {pares} e a quantidade de impares é {impares}")