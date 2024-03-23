#Exercício 8
#Acrescente as seguintes mensagens à solução do exercício anterior conforme o caso:
#- Caso o número de lados seja inferior a 3 escrever NÃO É UM POLÍGONO.
#- Caso o número de lados seja superior a 5 escrever POLÍGONO NÃO IDENTIFICADO.
num_lados = int(input("Digite o número de lados do seu polígono: "))
med_lados = float(input("Digite a medida dos lados em centímetros: "))

if num_lados < 3:
    print("Não é um polígono")
elif num_lados == 3:
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
    print("Polígono não identificado")


#exercício 8 de outra forma
lados = int(input("Diga o número de lados: "))
forma = ''
if lados < 3:
    print("Não é um polígono")
elif lados == 3:
    forma = "Triângulo"
elif lados == 4:
    forma = "Quadrado"
elif lados == 5:
    forma = "Pentágono"
else:
    print("Polígono não identificado")
if forma:
    medida = int(input("Diga a medida do lado: "))
    perimetro = lados*medida
    print(f"O seu polígono é um {forma} e seu perímetro é {perimetro}")


#exercício 8 de mais uma forma
lados = int(input("Diga o número de lados: "))
if lados < 3:
    print("Não é um polígono")
elif lados > 5:
    print("Polígono não identificado")
else:
    if lados == 3:
        forma = "Triângulo"
    elif lados == 4:
        forma = "Quadrado"
    else:
        forma = "Pentágono"
    medida = int(input("Diga a medida do lado: "))
    perimetro = lados*medida
    print(f"O seu polígono é um {forma} e seu perímetro é {perimetro}")
