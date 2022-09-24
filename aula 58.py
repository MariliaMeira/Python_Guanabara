#computador escolher um numero e o uisuario adivinhar
from random import randint
computador=randint(0,10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que voce consegue adivinhar qual foi? ')
acertou=False
palpite=0
while not acertou:
    jogador=int(input('Qual é o seu palpite? '))
    palpite+=1
    if jogador==computador:
        acertou=True
    else:
        if jogador<computador:
            print('Mais...')
        elif jogador >computador:
            print('Menos...')

print(f'Aceertou, com {palpite} palpites. Parabéns')
