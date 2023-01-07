primeiro = int(input('Digite o primeiro termo da sua PA: '))
razao = int(input('Digite a razão da sua PA: '))

cont = 1
termo = primeiro
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print(termo, end=' > ')
        cont += 1
        termo += razao
    print('FIM')
    mais = int(input('Quantos termos a mais você deseja em sua PA: '))
print(f'O total de termos de sua PA é: {total}')
