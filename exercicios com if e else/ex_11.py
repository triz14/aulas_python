#Exercício 11
#Escreva um programa que leia o valor de 3 ângulos de um triângulo e escreva se o triângulo é Acutângulo, Retângulo ou Obtusângulo. Sendo que:
#- Triângulo Retângulo: possui um ângulo reto. (igual a 90º)
#- Triângulo Obtusângulo: possui um ângulo obtuso. (maior que 90º)
#- Triângulo Acutângulo: possui três ângulos agudos. (menor que 90º)
angulo = int(input("Digite o valor dos ângulos do seu triângulo"))

if angulo == 90:
    print("Triângulo retângulo")
elif angulo > 90:
    print("Triângulo Obtusângulo")
else:
    print("Triângulo Acutângulo")