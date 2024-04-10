a = 80000
b = 200000
ano = 0

while a < b:
    a += a*0.3
    b += b*0.15
    ano += 1
print(f"O numero de anos foi {ano}")
