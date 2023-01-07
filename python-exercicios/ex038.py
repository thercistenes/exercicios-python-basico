num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
print(' ' * 15)

if num1 > num2:
    print('O PRIMEIRO número é MAIOR.')
elif num2 > num1:
    print('O SEGUNDO número é MAIOR.')
else:
    print('Os dois números são IGUAIS.')
