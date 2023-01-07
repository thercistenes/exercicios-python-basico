nome = str(input('Digite seu nome: ')).strip()
print('Seu nome em maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em minuúscula é: {}'.format(nome.lower()))
print('Seu nome tem {} letras.'.format(len(nome) - nome.count(' ')))
separa = nome.split()
#o split joga dentro de uma lista os nomes inteiros.
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))