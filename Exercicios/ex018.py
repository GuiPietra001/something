import math
ângulo = float(input('Digite o Ângulo que você deseja: '))
seno = math.sin(math.radians(ângulo))
print('O Ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))
print('O ângulo de {} tem a TANGANTE de {:.2f}'.format(ângulo, tangente))