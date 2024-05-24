# Jeito que o prof sugeriu
sequencia = [0,1,1,0,1,0,0,1,1,1,0,1,0,1,1]
#sub_seq = [0,1,1]
#sub_seq = [0,1,0]
sub_seq = [1,0,1]
qtd = 0

for i in range(len(sequencia) - len(sub_seq) + 1):
    flag = False
    for j in range(len(sub_seq)):
        if sequencia[i+j] != sub_seq[j]:
            flag = True
            break
    if flag == True:
        continue
    qtd += 1
print(qtd)
