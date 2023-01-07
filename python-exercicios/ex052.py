num = int(input('Digite um número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\33[34m', end=' ')
        total += 1
    else:
        print('\33[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\33[mO número {} foi divisível {} vezes.'.format(num, total))
if total == 2:
    print('O número {} É PRIMO.'.format(num))
else:
    print('O número {} NÃO É PRIMO.'.format(num))
