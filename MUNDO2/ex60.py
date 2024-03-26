n = int(input("Digite um número qualquer: "))
c = n
resultado=1
while c > 0:
    resultado*=c
    c -= 1
print(f"O fatorial de {n}! é igual a {resultado}")
