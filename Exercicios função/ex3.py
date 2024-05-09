def podeVotar(nome, ano_nascimento):
    idade = calculaIdade(ano_nascimento)
    a = 12
    if idade >= 16:
        print(f"Sim, a pessoa {nome} pode votar")
        return True
    else:
        print(f"Não, a pessoa {nome} ainda não pode votar")
        return False
        
def calculaIdade(ano_nascimento):
    return 2024-ano_nascimento
    
        
a = podeVotar("Lucas",2004)
b = podeVotar("Rafael",1996)
c = podeVotar("Gabriela",2014)