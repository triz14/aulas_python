#Estruturas de if e else (minha lógica)
idade = int(input("Digite sua idade: "))
if idade < 18:
     print("Você não pode usar o zé delivery")
else:
     print("Bem vindo ao zé delivery")

idoso = input("Você é idoso? ")
gestante = input("Você é gestante? ")

#Com o or somente uma condição precisa ser verdadeira
if idoso == 'sim' or gestante == 'sim':
     print("Pode estacionar")

#Com o and as duas ou mais condições precisam ser verdadeiras
idoso = input("Você é idoso? ")
cartao = input("Você tem o cartão? ")
if idoso == 'sim' and cartao == 'sim':
     print("Pode estacionar")

#Minha lógica
letra = input("Digite uma letra: ")
if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
     print("Você digitou uma vogal 🙃")
else:
     print("Você Digitou uma consoante 😒")

#Lógica explicada pelo professor
vogal = False
if letra == 'a':
    print(f"{letra} é uma vogal!")
    vogal = True
if letra == 'e':
    print(f"{letra} é uma vogal!")
    vogal = True
if letra == 'i':
    print(f"{letra} é uma vogal!")
    vogal = True
if letra == 'o':
    print(f"{letra} é uma vogal!")
    vogal = True
if letra == 'u':
    print(f"{letra} é uma vogal!")
    vogal = True
if not vogal:
    print(f"{letra} é consoante") 

letra = input("Digite uma letra: ")
resultado = 'Vogal'

if letra == 'a':
    print(resultado)
elif letra == 'e':
    print(resultado)
elif letra == 'i':
    print(resultado)
elif letra == 'o':
    print(resultado)
elif letra == 'u':
    print(resultado)
else:
    print("Consoante")