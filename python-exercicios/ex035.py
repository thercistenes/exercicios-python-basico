print('-=-' * 20)
print('Analisador de triângulos')
print('-=-' * 20)
lado1 = float(input('Digite o primeiro lado: '))
lado2 = float(input('Digite o segundo lado: '))
lado3 = float(input('Digite o terceiro lado: '))
if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado1 + lado3 > lado2:
    print('As medidas podem formar um triângulo!')
else:
    print('As medidas NÃO podem formar um triângulo!')
