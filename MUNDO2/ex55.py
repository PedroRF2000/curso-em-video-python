maiorPeso=0
menorPeso=0
for pessoas in range(0,5):
    peso=float(input("Digite o seu peso: "))
    if pessoas==1:
        maiorPeso=peso
        menorPeso=peso
    else:
        if peso>maiorPeso:
            maiorPeso=peso
        elif peso<menorPeso:
            menorPeso=peso
print(f"O maior peso lido foi {maiorPeso} kg.")
print(f"O menor peso lido foi {menorPeso} kg.")