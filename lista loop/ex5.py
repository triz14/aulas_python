n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

while n2<n1:
	print("Números inválidos")
	n1 = int(input("Digite o primeiro número: "))
	n2 = int(input("Digite o segundo número: "))
else:
	for i in range(n1, n2, 1):
		print(i)