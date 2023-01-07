n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

opcao = 0

while opcao != 5:
    print('''        [ 1 ] SOMAR
        [ 2 ] MUTIPLICAR
        [ 3 ] MAIOR 
        [ 4 ] NOVOS NÚMEROS
        [ 5 ] FINALIZAR PROGRAMA''')
    opcao = int(input('>>>>> Digite sua opção: '))

    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}.'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O produto entre {} e {} é {}'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print('entre {} e {} o maior é {}.'.format(n1, n2, maior))
        elif n1 < n2:
            maior = n2
            print('Entre {} e {} o maior é {}.'.format(n1, n2, maior))
        elif n1 == n2:
            print('Os dois números são iguais')
    elif opcao == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalisando programa...')
    else:
        print('Opção inválida. Tente novamente.')
    print('-=' * 10)

print('Final do programa!')
