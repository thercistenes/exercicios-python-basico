numeros = ('Zero', 'Um', 'Dois', 'tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    while True:
        digite = int(input('Digite um número entre 0 e 20: '))
        if 0 <= digite <= 20:
            break
        else:
            print(f'TENTE NOVAMAENTE!', end=' ')
    print(f'Você digitou o número "{numeros[digite]}"') 
    continuar = str(input('Deseja continuar? [S/N]? ')).strip().upper()[0]
    if continuar in 'N':
        break
print('-=' * 30)
print('Fim do programa')
