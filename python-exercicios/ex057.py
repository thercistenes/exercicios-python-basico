genero = str(input('Digite seu gênero [M/F]: ')).strip().upper()
while genero not in ['M', 'F']: #para fazer com uma string usar o "in" para ligá-las
        genero = str(input('Dados inválidos. Digite seu gênero corretamente [M/F:] ')).strip().upper()
if genero == 'M':
    print('Gênero MASCULINO digitado corretamente.')
elif genero == 'F':
    print('Gênero FEMININO digitado corretamente.')

