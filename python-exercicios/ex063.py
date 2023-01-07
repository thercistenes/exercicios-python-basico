print('=' * 15)
print('SEQUÊNCIA DE FIBONATI')
print('=' * 15)

num = int(input('Quantos termos deve ter a sua sequência de Fibonacci? '))
t1 = 0
t2 = 1
cont = 3
print(f'{t1} {t2}', end=' ')
while cont <= num:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(f'{t3}', end=' ')
    cont += 1
