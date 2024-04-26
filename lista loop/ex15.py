'''Em uma eleição presidencial existem quatro candidatos. Os votos são informados
por meio de código. Os códigos utilizados são:
1 , 2, 3, 4 - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o
conjunto de votos tem-se o valor zero.'''

# 1º tentativa

voto = int(input("Em quem você deseja votar? 1- Duda 2- Rafa 3- Bella 4- Bia 5- Carol\n6- Nulo 7- Brnaco e 0- sair: "))
duda = 0
rafa = 0
bella = 0
bia = 0
carol = 0
nulo = 0
branco = 0
votos = 0

while voto != 0:
    voto = int(input("Em quem você deseja votar? 1- Duda 2- Rafa 3- Bella 4- Bia 5- Carol\n6- Nulo 7- Brnaco e 0- sair: "))
    if voto == 1:
        duda += 1
    elif voto == 2:
        rafa += 1
    elif voto == 3:
        bella += 1
    elif voto == 4:
        bia += 1
    elif voto == 5:
        carol += 1
    elif voto == 6:
        nulo +=1
    elif voto == 7:
        branco += 1
    elif voto == 0:
        break
    votos += 1
print(f"Duda recebeu {duda} votos, Rafa recebeu {rafa} votos, Bella recebeu {bella} votos,\nBia recebeu {bia} votos, Carol recebeu {carol} votos, nulos receberam {nulo} votos, branco recebeu {branco} votos\nA porcentagem dos votos nulos foi {nulo/votos*100}% e a porcentagem de brancos foi {branco/votos*100}%")