a = int(input('Digite um valor: '))
b = int(input('Digite um segundo valor: '))
c = int(input('Digite um terceiro valor: '))
# Soluções para o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Soluções para o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O número menor é: {}'.format(menor))
print('O número maior é: {}.'.format(maior))
