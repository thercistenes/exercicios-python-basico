listanum = []
maior = menor = 0

for c in range(0, 4):
    listanum.append(int(input(f'Digite um número na posição  {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if maior > listanum[c]:
            maior = listanum[c]
        if menor < listanum[c]:
            menor = listanum[c]
            
print(f'O maior número é {maior} e está na posição: ', end=' ')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}...', end=' ')
print()
print(f'O menor número é {menor} e está na posição: ', end=' ')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end=' ')
