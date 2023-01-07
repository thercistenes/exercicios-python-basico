largura = float(input('Insira a largura da parede: '))
altura = float(input('Insira a altura da parede: '))
area = largura * altura
tinta = area / 2
print('A área da sua parede é {}m² e é necessário {}l de tinta para pintá-la.'.format(area, tinta))
