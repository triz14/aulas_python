i = 0
pares = 0
while i < 10:
    num = int(input(f"Diga o {i+1}º número: "))
    if num%2==0:
        pares += 1
    i+=1
print(f"Vc digitou {pares} pares e {i - pares} impares")

