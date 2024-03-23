resp = input("Diga sim ou não (s/n): ")
while resp != 's' and resp != 'n':
    resp = input("Diga sim ou não (s/n): ")
if resp == 's':
    print("SIIIIM")
else:
    print("NÃAAAO")

#outro jeito
resp = input("Diga sim ou não (s/n): ")
while not (resp == 's' or resp == 'n'):
    resp = input("Diga sim ou não (s/n): ")
if resp == 's':
    print("SIIIIM")
else:
    print("NÃAAAO")