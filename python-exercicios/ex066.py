quant = soma = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    quant += 1
    soma += num
print(f'Você digitou {quant} números e a soma entre eles foi {soma}')