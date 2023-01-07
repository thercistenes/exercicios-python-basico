from datetime import date
atual = date.today().year
nasc = int(input('Digite seu ano de nascimento: '))
idade = atual - nasc
if idade == 18:
    print('Você tem {} anos, aliste-se IMEDIATAMENTE!'.format(idade))
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print('Você tem {} anos, ainda falta {} anos para seu alistamento.'.format(idade, saldo))
    print('Seu ano de alistamento será: {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    ano =  atual - saldo
    print('Você tem {} anos, o tempo de alistamento passou {} anos.'.format(idade, saldo))
    print('Seu ano de alistamento foi: {}.'.format(ano))
