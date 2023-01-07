num = int(input('Digite um número para ver seu fatorial [ n! ]: '))
cont = num
fat = 1
while cont > 0:
   print(cont, end=' ')
   if cont > 1:
      print('x', end=' ')
   else:
      print('=', end=' ')
   fat = fat * cont
   cont -= 1
print(fat)