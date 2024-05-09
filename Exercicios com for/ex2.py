# peça 10 numeros ao usuario e faça a soma e a media

soma = 0

for i in range(10):
    num = input("Digite um número: ")
    while not num.isnumeric():
        print("Valor inválido")
        num = input("Digite um número: ")
    num = int(num)
    soma += num
media = soma/10
print(f"A soma dos números é {soma} e a média é {media}")