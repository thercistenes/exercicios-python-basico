distancia = float(input('Qual a distância em kilômetros da sua viajem? '))
viajem1 = distancia * 0.5
viajem2 = distancia * 0.45
if distancia <= 200:
    print('O preço da sua viajem é: R$ {:.2f}'.format(viajem1))
else:
    print('O preço da sua viajem é: R$ {:.2f}'.format(viajem2))
