import random
print('Vou pensar em um número de 0 a 5, tente advinhar...')
juz = random.randint(0, 5)
jekha = int(input('Em qual número eu pensei? '))

if jekha == juz:
    print('Parabéns, você acertou!')
else:
    print('Você errou!')
