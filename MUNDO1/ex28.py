from random import randint
import emoji
from time import sleep
print(emoji.emojize("Computador, penserá em um número entre 0 e 5 :thinking_face:"))
numero = [0, 1, 2, 3, 4, 5]
numeroPensado = randint(numero)


numeroUsuario = int(
    input("Digite um número de 0 a 5, e tente descobrir se você acertou: "))
print("O computador está processando um valor ...")
sleep(3)
if numeroUsuario == numeroPensado:
    print("Parabéns, você VENCEU que foi {}!".format(numeroPensado))
else:
    print("Você PERDEU ! O número escolhido pelo computador foi {}".format(numeroPensado))
