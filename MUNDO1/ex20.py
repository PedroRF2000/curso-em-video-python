from random import shuffle
aluno1 = input("Aluno: ")
aluno2 = input("Aluno: ")
aluno3 = input("Aluno: ")
aluno4 = input("Aluno: ")
listaDeAlunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(listaDeAlunos)
print("A ordem de apresentação dos trabalhos ficou: {}".format(listaDeAlunos))
