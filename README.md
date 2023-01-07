# exercicios-python-basico
 Propostas de resolução para exercícios de python do canal Curso em Vídeo
 
 # EX083
*Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.*
 
**expr = str(input('Digite a expressão: ')).strip()** *//Expressão que vai receber o input*
**pilha = []** *//Esta lista vai receber os comandos para a validação da expressão*

**for simb in expr:** *//Este loop vai percorrer a expressão: "Para todo símbolo que está na expressão:*
    **if simb == '(':** *//A primeira possibilidade é o array receber da 'expr' o símbolo '('*
        **pilha.append('(')** *//Quando o '(' estiver na expressão imediatamente ele será colocado pelo 'append' na última posição*
    **elif simb == ')':** *//Para o exercício, as duas possibilidades paro o '(', serão 0 ou mais*
        **if len(pilha) > 0:** *//Assim que for dectado um ')', o laço vai rodar e caso a pilha tenha algo dentro ela vai tirar o último elemento. O laço será repetido caso tenha-se outro elemento. Na prática o que tá acontecendo é que se a quantidade de '('  e ')' não forem iguais o pop não vai retirar os sobressalente e se terá um parênteses ou mais a mais*
            **pilha.pop()** *//o método pop é que vai retirar o último elemento do pilha, dentro da condição de encontrar um '('*
        **else:** *//este é o caso de a pilha está vazia, então ele vai acrescentar um parenteses, isso significa que no próximo loop caso não se encontre outro para para fazer o pop a estrutura termina > 0 e a expressão está errada.*
            **pilha.append(')')**
            **break**
**if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')**

