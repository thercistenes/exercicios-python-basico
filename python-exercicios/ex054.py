from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    nasc = int(input('Qual ano a {}ª pessoa nasceu?'.format(c)))
    idade = atual - nasc
    if idade >= 18:
        maior =+ 1
    else:
        menor += 1
print('{} MAIORES. {} MENORES'.format(maior, menor))
