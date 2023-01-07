somaidade = 0
nomevelho = ''
idademaisvelho = 0
qtdmulheres20 = 0

for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('NOME: ')).strip().upper()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [ M/F ]: ')).strip().upper()

    somaidade += idade

    if p == 1 and sexo in 'Mm':
        nomevelho = nome
        idademaisvelho = idade
    if idade > idademaisvelho and sexo in 'Mm':
        nomevelho = nome
        idademaisvelho = idade
    if sexo in 'Ff' and idade < 20:
        qtdmulheres20 += 1

media = somaidade / 4

print('A média de idade do grupo é {:.2f}'.format(media))
print('O homem mais velho é {} e ele tem {} anos'.format(nomevelho, idademaisvelho))
print('A quantidade de mulheres abaixo dos 20 anos é: {}'.format(qtdmulheres20))
