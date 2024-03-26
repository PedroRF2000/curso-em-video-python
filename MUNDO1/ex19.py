#  Desafio 19
from random import choice
aluno1=input("O nome do 1ª aluno é: ")
aluno2=input("O nome do 2ª aluno é: ")
aluno3=input("O nome do 3ª aluno é: ")
aluno4=input("O nome do 4ª aluno é: ")
listaDeAlunos=[aluno1,aluno2,aluno3,aluno4]
alunoEscolhido=choice(listaDeAlunos)
print("O aluno escolhido para limpar o quadra foi {} .".format(alunoEscolhido))