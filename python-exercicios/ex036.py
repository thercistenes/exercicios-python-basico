casa = float(input('Qual o valor da casa? R$ '))
sal = float(input('Qual seu salário? R$ '))
par = int(input('Em quantos anos você vai pagar? '))

mesalidade = par * 12
parcelacasa = casa / mesalidade
porsalario = sal * (30 / 100)

print('Valor da prestação: R$ {:.2f}'.format(parcelacasa))
print('-=-' * 20)
if parcelacasa <= porsalario:
    print('Empréstimo CONCEDIDO.')
else:
    print('Empréstimo NEGADO.')
print('-=-' * 20)
