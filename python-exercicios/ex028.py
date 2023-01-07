from random import randint
from time import sleep
computador = randint(0, 2)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 2, tente advinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('VENCEU!')
else:
    print('Você PERDEU! Eu pensei no número {}'.format(computador))
