num = int(input('Digite um número: '))
print('''Escolha uma das opções abaixo: 
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print('O número {} em Binário é: {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O número {} em Octal é: {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O número {} em Hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')
