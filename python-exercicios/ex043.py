peso = float(input('Digite seu peso em kilo: '))
altura = float(input('Digite seu peso em metros: '))
imc = peso / (altura ** 2)
print('Seu IMC é igual a {:.2f}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso.')
elif imc < 25:
    print('Peso ideal.')
elif imc < 30:
    print('Sobrepeso.')
elif imc < 40:
    print('Obesidade.')
elif imc >= 40:
    print('Obesidade mórbida.')
