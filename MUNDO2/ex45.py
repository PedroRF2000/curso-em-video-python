from random import choice
from time import sleep
opçõesJogada = ["pedra", "papel", "tesoura"]
print("Pedra , papel e tesoura")
sleep(1)
minhaMão = input("Eu joguei: ").lower()
computadorMão = choice(opçõesJogada).lower()
print("O computador: ",computadorMão)
if minhaMão=="pedra" and computadorMão=="pedra" or minhaMão=="papel" and computadorMão=="papel" or minhaMão=="tesoura" and computadorMão=="tesoura":
    print("Deu impate , vamos jogar mais uma vez.")
elif minhaMão=="pedra" and computadorMão=="papel" or minhaMão=="papel" and computadorMão=="tesoura" or minhaMão=="tesoura" and computadorMão=="pedra":
    print("O computador ganhou! Vamos jogar mais uma vez.")
else:
    print("Ganhei! Vamos jogar de novo.")