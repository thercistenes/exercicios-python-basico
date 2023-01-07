primeiro = int(input('Digite o primeiro termo da sua PA: '))
razao = int(input('Qual a razão da sua PA? '))

cont = 1
termo = primeiro

while cont <= 10:
   print(termo, end=' > ')
   termo += razao
   cont += 1
print('Fim...')
