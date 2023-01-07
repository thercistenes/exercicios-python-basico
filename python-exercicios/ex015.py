dias = int(input('Digite a quantidade de dias que ficou com o carro: '))
km = float(input('Quantidade de quilômetros rodados: '))
qtddias = dias * 60
qtdkm = km * 0.15
total = qtddias + qtdkm
print('O valor gasto de diárias é R${:.2f}, de km rodados foi R${:.2f}'.format(qtddias, qtdkm))
print('O valor total a pagar é de R${:.2f}'.format(total))
