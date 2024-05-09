def calculaIdade(nome,ano_nascimento):
	idade  = 2024-ano_nascimento
	print(f"A pessoa {nome} tem a idade {idade}")
	return idade
	    
	        
a = calculaIdade("Lucas",2004)
b = calculaIdade("Rafael",1996)
c = calculaIdade("Gabriela",2014)

# Outra forma de fazer
ano_atual = 2024      
	
def calculaIdade(nome,ano_nascimento):
    idade  = ano_atual-ano_nascimento
    print(f"A pessoa {nome} tem a idade {idade}")
    return idade
	    	        
a = calculaIdade("Lucas",2004)
b = calculaIdade("Rafael",1996)
c = calculaIdade("Gabriela",2014)

# Com a inclusão de uma biblioteca
from datetime import datetime
	
agora = datetime.now()
ano_atual = agora.year
		
def calculaIdade(nome,ano_nascimento):
    idade  = ano_atual-ano_nascimento
    print(f"A pessoa {nome} tem a idade {idade}")
    return idade
	            
a = calculaIdade("Lucas",2004)
b = calculaIdade("Rafael",1996)
c = calculaIdade("Gabriela",2014)