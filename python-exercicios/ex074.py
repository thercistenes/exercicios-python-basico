from random import randint
computador = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('VALORES SORTEADOS: ')
for n in computador:
    print(n, end=' ')
print(f'\nO maior valor sorteado foi: {max(computador)}')
print(f'O menor valor sorteado foi: {min(computador)}')
