média = 0
idadeHomemVelho = 0
mulheresMenores = 0
nomeVelho=""
cont=1
for pessoa in range(1, 5):
    print(f"Informe os dados da {pessoa}ª pessoa.")
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade:"))
    sexo = input("Digite o sexo: ").lower()

    média += idade/4
    if pessoa == 1 and sexo == "mas":
        idadeHomemVelho = idade
        nomeVelho=nome
    else:
        if idade > idadeHomemVelho:
            idadeHomemVelho = idade
            nomeVelho = nome
    if idade<20 and sexo == "fem":
        mulheresMenores+=1




print(f"A média de idade do grupo é de {média} anos.")
print(f"O nome do homem mais velho é {nomeVelho} com {
      idadeHomemVelho} anos de idade.")
print(f"O número de mulheres com menos de 20 anos é de {mulheresMenores}.")
