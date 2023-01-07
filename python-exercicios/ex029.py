vel = float(input('Qual a velocidade atual do seu carro? '))
multa = (vel - 80) * 7
if vel <= 80:
    print('Siga em segurança!!!')
else:
    print('A velocidade excedeu o limite de 80km, você foi multado!')
    print('Sua multa é: R${:.2f}'.format(multa))
