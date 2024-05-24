# Jeito que o nando sugeriu
sequencia = [0,1,1,0,1,0,0,1,1,1,0,1,0,1,1]
#sub_seq = [0,1,1]
#sub_seq = [0,1,0]
sub_seq = [1,0,1]
indices = []
for i in range(len(sequencia)):
    if sequencia[i] == sub_seq[0] and i <= len(sequencia) - 3:
        indices.append(i)
print(indices)
j = 0
novo_indices = indices[:]
for i in novo_indices:
    print(f"sequencia[{i}+1] = {sequencia[i+1]}, sub = {sub_seq[1]}")
    if sequencia[i+1] != sub_seq[1]:
        #print(f"O item da sequencia é {sequencia[i]} no local {i}")
        indices.pop(j)
    j += 1
print(indices)
j = 0
novo_indices = indices[:]
for i in novo_indices:
    if sequencia[i+2] != sub_seq[2]:
        indices.pop(j)
    j += 1
print(indices)
print(len(indices))