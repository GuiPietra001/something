from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] Tesoura  
''')

jogador = int(input('Qual vai ser a sua jogada? '))

print('-=' * 10)
print('O computador escolheu {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 10)

if computador == 0:
    if jogador == 0:
        print('Empate')
        pass  # Lógica para empate
    elif jogador == 1:
        print('Jogador vence')
        pass  # Lógica para jogador vence
    elif jogador == 2:
        print('Computador vence')
        pass  # Lógica para computador vence
    else:
        print('Jogada inválida!')

elif computador == 1:
        print('Jogador vence')
    if jogador == 0:
        pass  # Lógica para computador vence
    elif jogador == 1:
        pass  # Lógica para empate
    elif jogador == 2:
        pass  # Lógica para jogador vence
    else:
        print('Jogada inválida!')
    
elif computador == 2:   
    if jogador == 0:
        pass  # Lógica para jogador vence
    elif jogador == 1:
        pass  # Lógica para computador vence
    elif jogador == 2:
        pass  # Lógica para empate
    else:
        print('Jogada inválida!')
