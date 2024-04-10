while True:
    nota = input("Digite uma nota entre 0 e 10: ")
    if nota.isnumeric():
        if int(nota) >= 0 and int(nota) <= 10:
            nota = int(nota)
            break
        print("Número inválido")
    else:
        print("Valor inválido")

