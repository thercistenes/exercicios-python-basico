listagem = ('Caderno', 15, 'Caneta', 20,'Lápis', 3, 'Estojo', 25)
for item in range(0, len(listagem)):
    if item % 2 == 0:
        print(f'{listagem[item]:.<30}', end=' ')
    else:
        print(f'{listagem[item]:>5.2f}')
