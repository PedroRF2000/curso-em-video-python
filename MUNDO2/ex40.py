
n1 = float(input("O aluno tirou na 1ª prova: "))
n2 = float(input("O aluno tirou na 2ª prova: "))
média = (n1+n2)/2
if média < 5:
    print("REPROVADO!")
elif média < 7:
    print("RECUPERAÇÃO!")
else:
    print("APROVADO!")
