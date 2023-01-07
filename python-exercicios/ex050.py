soma = 0
cont = 1
for c in range(1, 7):
    num = int(input('Digite o {}° valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você digitou {} números pares e a soma entre eles foi {}'.format(cont - 1, soma))
