#Exercício 10
#Escreva um programa que leia as medidas dos lados de um triângulo e escreva se ele é Equilátero, Isósceles ou Escaleno. Sendo que:
#- Triângulo Equilátero: possui os 3 lados iguais.
#- Triângulo Isósceles: possui 2 lados iguais.
#- Triângulo Escaleno: possui 3 lados diferentes.
lado_1 = int(input("Digite a medida de um lado do seu triângulo: "))
lado_2 = int(input("Digite a medida de outro lado do seu triângulo: "))
lado_3 = int(input("Digite a medida de mais um lado do seu triângulo: "))

if lado_1 == lado_2 and lado_1 == lado_3:
    print("Equilátero")
elif (lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3) and (lado_1 != lado_2 or lado_1 != lado_3 or lado_2 == lado_3):
    print("Isóceles")
else:
    print("Escaleno")