for c in range (1,4):
    n = float(input(f"Informe o {c}ª número: "))
    if c==0:
        maior=n
        if n>maior:
            maior=n
print(f"O maior número é {maior}")
print("FIM")