lista = []
pares = []
impares = []

while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar: [S/N] ')).upper().strip()[0]
    if resp != 'SN':
        print('Opção inválida, tente novamente!')
    elif resp == 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)

print(f'Os valores digitados foram: {lista}')
print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores ímpares digitados foram: {impares}')


