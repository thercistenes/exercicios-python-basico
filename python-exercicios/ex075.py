while True:
    valor = (int(input('Digite o primeiro valor: ', )), int(input('Digite o outro valor: ' )), int(input('Digite o mais um valor: ')), int(input('Digite o último valor: ')))
    print(f'Você digitou {valor}')
    if 9 in valor:
        print(f'O número 9 apareceu {valor.count(9)} vezes.')
    else:
        print('O número 9 não foi digitado')
    if 3 in valor:
        print(f'O número 3 apareceu na {valor.index(3) + 1}ª posição.')
    else:
        print('O número 3 não foi digitado')
    print('Os números pares foram: ', end='')
    for n in valor:
        if n % 2 == 0:
            print(n, end=' ')
    continuar = str(input('\nDeseja Continuar? [S/N] ')).strip().upper()[0]
    if 'N' in continuar:
        break
print('FIM DO PROGRAMA')
