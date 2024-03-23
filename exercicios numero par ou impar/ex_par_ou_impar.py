num = 2

if num%2 == 0:
    print(f"{num} é par pois {num} % {2} = {num%2}")
else:
    print(f"{num} é impar pois {num} % {2} = {num%2}")

num = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite mais um número: "))
num4 = int(input("Digite outro número: "))
num5 = int(input("Digite outro número: "))
count = 0

if num%2 == 0:
    count += 1
if num2%2 == 0:
    count += 1
if num3%2 == 0:
    count += 1
if num4%2 == 0:
    count += 1
if num5%2 == 0:
    count += 1
qt_impares = 5-count
print(f"A quantidade de pares é {count} e a quantidade de impares é {qt_impares}")