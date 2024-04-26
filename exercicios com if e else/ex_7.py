#Exercício 7
#Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm). Calcular e imprimir o seguinte:
#- Se o número de lados for igual a 3 escrever TRIÂNGULO e o valor da área.
#- Se o número de lados for igual a 4 escrever QUADRADO e o valor da sua área.
#- Se o número de lados for igual a 5 escrever PENTÁGONO.
num_lados = int(input("Digite o número de lados do seu polígono: "))
med_lados = float(input("Digite a medida dos lados em centímetros: "))

if num_lados == 3:
    area = (med_lados ** 2) * (3 ** 0.5)/4
    print("Triângulo")
    print(f"A area do seu triângulo é {area}")
elif num_lados == 4:
    area = med_lados ** 2
    print("Quadrado")
    print(f"A area do seu quadrado é {area}")
elif num_lados == 5:
    print("Pentágono")
else:
    print("Digito errado refaça por favor")