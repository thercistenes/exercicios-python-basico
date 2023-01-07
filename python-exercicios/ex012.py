preco = float(input('Insira o preço do produto: '))
desconto = float(input('Insira o percentual de desconto: '))
promocao = preco - ((preco * desconto) / 100)
print('O valor do produto com o desconto de {}% é {}.'.format(desconto, promocao))
