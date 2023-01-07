**#EXERCÍCIO 083**
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expr = str(input('Digite a expressão: ')).strip() *Este é o input padrão que vai receber a expressão a ser validade.*
pilha = [] *O Array aqui vai servir para receber os parâmetros para a validação do exercício*
for simb in expr: 
    if simb == '(': 
        pilha.append('(') 
    elif simb == ')': 
        if len(pilha) > 0: # 
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')