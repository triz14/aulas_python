v = int(input("Digite a velocidade: "))

if v <= 100:
    print("Isento")
else:
    if v <= 120:
        multa = 0.2*v
    elif v <= 150:
        multa = 0.2*120 + 0.3*v
    else:
        multa = 0.2*120 + 0.3*150 + 0.4*v
    print(f"Sua multa é {multa:.2f}")