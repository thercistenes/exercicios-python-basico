a = float(input('Digite o primeiro lado: '))
b = float(input('Digite o segundo lado: '))
c = float(input('Digite o terceiro lado: '))

if a + b > c and a + c > b and b + c > a:
    print('Pode formar um triângulo ', end='')
    if a == b == c:
       print('EQUILÁTERO.')
    elif a == b != c or a == c != b or b == c != a:
        print('ISÓSCELES.')
    elif a != b != c or a != c != b or b != c != a:
        print('ESCALENO.')
else:
    print('Não forma um triângulo.')
