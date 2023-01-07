from random import randint
computador = randint(0, 10)

print('Olá sou seu computador vou pensar em número de 0 a 10.')
print('Você consegue advinhar?')

tentativas = 0
acertou = False

while not acertou:
    jogador = int(input('Qual seu palpite? '))
    tentativas += 1
    if computador == jogador:
        acertou = True
    else:
        if jogador > computador:
            print('MENOS... Tente outra vez1')
        elif jogador < computador:
            print('MAIS... Tente outra vez!')
print('Você acertou em {} tentativas.'.format(tentativas))
