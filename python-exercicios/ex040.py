nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('A média do aluno foi {:.1f}'.format(media))

if media < 5:
    print('REPROVADO!')
elif 7 > media >= 5:
    print('RECUPERAÇÃO!')
elif media >= 7:
    print('APROVADO!')
