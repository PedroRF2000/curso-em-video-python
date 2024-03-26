somaDosPares=0
for i in range(1,7):
    n = int(input(f"Digite o {i}ª número: "))
    if n%2==0:
        somaDosPares+=n
print(f"A soma dos número pares é igual a {somaDosPares}")

