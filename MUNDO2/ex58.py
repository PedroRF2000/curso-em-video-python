from random import randint
import emoji
from time import sleep

tentativas=0
numeroPensado = randint(0,10)
print(emoji.emojize("Computador, penserá em um número entre 0 e 10 :thinking_face:"))

numeroUsuario = int(input("Digite um número de 0 a 10, e tente descobrir se você acertou: "))
print("O computador está processando um valor ...")
sleep(1)

if numeroUsuario == numeroPensado:
    print(f"Parabéns, você tentou {tentativas} até acertar o número, o número pensando por você foi {numeroPensado}!")

while numeroPensado!=numeroUsuario:
    numeroUsuario = int(input(f"Você errou, tente novamente: "))
    print("O computador está processando um valor ...")
    sleep(1)
    tentativas+=1

if numeroUsuario == numeroPensado:
    print(f"Parabéns, você tentou {tentativas} até acertar o número, o número pensando por você foi {numeroPensado}!")
else:
    print(f"Você PERDEU ! O número escolhido pelo computador foi {numeroPensado}")
