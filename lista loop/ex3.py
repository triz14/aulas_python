a = 80000
b = 200000
ano = 0

while a < b:
    a += a*1.03
    b += b*1.015
    ano += 1
print(f"O numero de anos foi {ano}")
