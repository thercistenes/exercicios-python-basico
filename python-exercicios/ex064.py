posicao = 1
num = int(input(f'Digite o {posicao}º valor [999 para parar]: '))
cont = 0
soma = 0
while num != 999:
    soma += num
    posicao += 1
    cont += 1
    num = int(input(f'Digite o {posicao}º valor [999 para parar]: '))
print(f'Você digitou {cont} valores e a soma entre eles foi {soma}!')
