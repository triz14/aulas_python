'''Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem
caso o valor seja inválido e continue pedindo até que o usuário informe um valor
válido.'''

# 1º tentativa

'''while True:
    nota = input("Digite uma nota entre 0 e 10: ")
    if nota.isnumeric():
        if int(nota) >= 0 and int(nota) <= 10:
            nota = int(nota)
            break
        print("Número inválido")
    else:
        print("Valor inválido")'''

# 2º tentativa

while True:
    num = input("Digite uma nota entre 0 a 10: ")
    if num.isnumeric():
        num = int(num)
        if num >= 0 and num <= 10:
            break
        else:
            print("Número inválido")
    else:
        print("Valor inválido")

