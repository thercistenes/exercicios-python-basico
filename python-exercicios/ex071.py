print('=' * 30)
print('{:^30}'.format('BANCO TC'))
print('=' * 30)

valor = int(input('Valor do saque: R$ '))
total = valor
cedula = 50
qtdcedula = 0

while True:
    if total >= cedula:
        total -= cedula
        qtdcedula += 1
        #isso acontece enquanto o total de dinheiro disponível for maior do que a primeira cédula
    else:
        if qtdcedula > 0:
            print(f'{qtdcedula} Cédulas de {cedula:.2f}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 5
        elif cedula == 5:
            cedula = 1
        qtdcedula = 0
        if total == 0:
            break
