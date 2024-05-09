pares = 0
for i in range(1,11):
    num = input("Diga um numero: ")
    while not num.isnumeric():
        num = input("Diga um numero: ")
    num = int(num)
    if num % 2 == 0:
        pares += 1
print(f"Vc digitou {pares} pares e {i - pares} impares")