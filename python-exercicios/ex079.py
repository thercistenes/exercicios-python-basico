numeros = []
while True:
    n = int(input("Digite um número: "))
    if n not in numeros:
        numeros.append(n)
    else:
        print('Valor Inválido, JÁ ADICIONADO!')
    while True:
        continuar = str(input("Digite um continuar: [S/N] ")).strip().upper()[0]
        if continuar not in 'SN':
            print('COMANDO INVÁLIDO!')
        else:
            break
    if continuar in 'N':
            break
print(sorted(numeros, reverse=True))
