from datetime import date
ano = int(input('Digite um ano para saber se ele é bisexto, caso o ano seja o atual digite 0: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISEXTO.'.format(ano))
else:
    print('O ano {} NÃO É BISEXTO.'.format(ano))

