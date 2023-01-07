from random import randint
from time import sleep

print('=' * 5, '\33[^PAR ou ÍMPAR\33[m', '=' * 5)
print(' ')

qtd = 0

while True:
    computador = randint(0, 10)
    jogador = int(input('Sua jogada: '))
    total = computador + jogador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Você escolhe PAR ou  ÍMPAR? [ P/I ] ')).strip().upper()[0]
        print(' ')
    print(f'Você Jogou: {jogador} \nComputador Jogou: {computador} \nTotal: {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('\33[34mVocê VENCEU!!\33[m')
            print(' ' * 5, f'>>>{total} é PAR!')
            qtd += 1
        else:
            print('\33[31mVocê PERDEU!!!\33[m')
            print(' ' * 5, f'>>>{total} é PAR!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('\33[34mVocê VENCEU!!!\33[m')
            print(' ' * 5, f'>>>{total} é ÍMPAR!')
            qtd += 1
        else:
            print('\33[31mVocê PERDEU!!!\33[m')
            print(' ' * 5, f'>>>{total} é ÍMPAR!')
            break
    sleep(1)
    print('CONTINUE', end=' ')
    sleep(1)
    print('JOGANDO')
    sleep(1)
    print('\33[32m>>>>[ 1 ]<<<<\33[m')
    sleep(1)
    print('\33[33m>>>>[ 2 ]<<<<\33[m')
    sleep(1)
    print('\33[31m>>>>[ 3 ]<<<<\33[m')
    sleep(1)
    print('=' * 40)
print(' ')
print(f'Você venceu {qtd} partidas!')
print(' ')
sleep(1)
print('\33[31mGAME OVER!!!\33[m')
