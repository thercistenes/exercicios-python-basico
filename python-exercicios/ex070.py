print('{:=^40}'.format('LOJA SUPER BARATÃO'))

soma = maismil = menor = qtd = 0
menorproduto = ' '

while True:
    produto = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$ '))
    continuar = ' '
    soma += preco
    qtd += 1
    if qtd == 1:
        menor = preco
        menorproduto = produto
    elif preco < menor:
        menor = preco
        menorproduto = produto
    if preco > 1000:
        maismil += 1
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [ S/N ] ')).strip().upper()[0]
    if continuar == 'N':
        print('-' * 40)
        break
    print('-' * 40)

print(f'O produto mais barato foi {menorproduto} custando R$ {menor:.2f}')
print(f'Qtd produtos acima de R$ 1000,00: {maismil}')
print(f'O total da sua compra foi: R$ {soma:.2f}')
print('{:-^40}'.format('Fim do programa!'))
