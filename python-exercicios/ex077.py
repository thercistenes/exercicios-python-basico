palavras = ('horta', 'compostagem', 'grama', 'vaso', 'tulipa', 'cansaço', 'suor', 'lama', 'cheiro')
for item in palavras:
    print(f'\n{item} =', end= ' ')
    for letra in item:
        if letra in 'aeiou':
            print(letra, end=' ')