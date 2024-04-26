'''Supondo que a população de um país A seja da ordem de 80000 habitantes com
uma taxa anual de crescimento de 3% e que a população de B seja 200000
habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e
escreva o número de anos necessários para que a população do país A ultrapasse
ou iguale a população do país B, mantidas as taxas de crescimento.'''

# 1º tentativa

'''a = 80000
b = 200000
ano = 0

while a < b:
    a *=1.03
    b *=1.015
    ano += 1
print(f"O numero de anos foi {ano}")'''

# 2º tentativa

a = 80000
b = 200000
anos = 0

while b > a:
    a *= 1.03
    b *= 1.015
    anos += 1
print(f"Foi necessário {anos}")
