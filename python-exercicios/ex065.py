resp = 'S'
quant = media = soma = maior = menor = 0
while resp in 'S':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    media = soma / quant
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
print(f'Você digitou {quant} números, a soma entre eles é {soma}, a média entre eles é {media}')
print(f'O maior é {maior} e o menor é {menor}')
