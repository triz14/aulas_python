soma = 0
for i in range(1,11):
    num = input("Diga um numero: ")
    while not num.isnumeric():
        num = input("Diga um numero: ")
    num = int(num)
    soma += num
print(f"A soma é {soma} e a média é {soma/i}")