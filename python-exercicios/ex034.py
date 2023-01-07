sal = float(input('Digite seu salário: R$ '))
if sal > 1250:
    sal = sal + (sal * 10 / 100)
else:
    sal = sal + (sal * 15 / 100)
print('Seu salário com o aumento proporcional é R${:.2f}.'.format(sal))
