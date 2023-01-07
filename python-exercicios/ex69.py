pessoas = p18 = hcad = mulhermenor20 = 0

while True:
    idade = int(input('IDADE: '))
    genero = ' '
    continuar = ' '
    pessoas += 1
    while genero not in 'MF':
        genero = str(input('GÊNERO: [ M/F ] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [ S/N ] ')).strip().upper()[0]
    print('-' * 40)
    if idade >= 18:
        p18 += 1
    if genero == 'M':
        hcad += 1
    if idade < 20 and genero == 'F':
        mulhermenor20 += 1
    if continuar == 'N':
        break

print(f'Pessoas cadastradas {pessoas}')
print(f'Pessoas maiores de 18 anos: {p18}')
print(f'Homens cadastrados: {hcad}')
print(f'Mulheres menores de 20 anos: {mulhermenor20}')
print(' ')
print('FIM DO PROGRAMA')
