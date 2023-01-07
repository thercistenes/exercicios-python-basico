print('{:=^40}'.format(' THERCÍSTENES '))
preço = float(input('Preços das compras: R$ '))
print('''FORMAS DE PAGAMENTO:
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] Em até 2 vezes no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Digite uma opção: '))

if opção == 1:
    pgtfinal = preço - (preço * 10 / 100)
elif opção == 2:
    pgtfinal = preço - (preço * 5 / 100)
elif opção == 3:
    parcela = preço / 2
    print('Sua compra será divida em 2 parcelas de R$ {:.2f}'. format(parcela))
    pgtfinal = preço
elif opção == 4:
    qtdparcela = int(input('Digite a quantidade de parcelas desejada: '))
    parcela = preço / qtdparcela
    print('Sua compra será dividida em {} parcelas de R$ {:.2f}'.format(qtdparcela, parcela))
    pgtfinal = preço + (preço * 20 / 100)
else:
    print('Opção inválida, tente novamente!')
    pgtfinal = preço
print('Sua compra de R$ {:.2f} sairá por R$ {:.2f} no final.'.format(preço, pgtfinal))
