from math import sin, cos, radians, tan
angulo = float(input('Digite um ângulo: '))
seno = sin(radians(angulo))
print('O SENO de {} é: {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O COSSENO de {} é: {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('A TANGENTE de {} é : {:.2f}'.format(angulo, tangente))

