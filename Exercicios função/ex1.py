def podeVotar(nome, idade):
    if idade >= 16:
        print(f"Sim, a pessoa {nome} pode votar")
        return True
    else:
        print(f"Não, a pessoa {nome} ainda não pode votar")
        return False




a = podeVotar("Lucas",38)
print(f"a primeira resposta foi {a}")
b = podeVotar("Maira",13)
print(f"a segunda resposta foi {b}")
c = podeVotar("Pedro",18)