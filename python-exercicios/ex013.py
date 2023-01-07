salario = float(input('Insira o salário do funcionário: '))
aumento = float(input('Insira o percentual de aumento salaria: '))
remuneracao = salario + ((salario * aumento) / 100)
print('A remuneração final do funcionário é: R${:.2f}'.format(remuneracao))
