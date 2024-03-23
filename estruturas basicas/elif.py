#Aprendendo elif (elif é um código igual o if porém ele só será executado se as condições do primeiro if não forem compridas)
nota = int(input("Digite sua nota: "))
if nota > 6:
    print("Aprovado")
elif nota < 6 and nota >= 4:
    print("Exame")
else:
    print("Reprovado")