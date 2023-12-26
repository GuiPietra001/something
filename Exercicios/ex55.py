maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input('Digite o peso da {}º Pessoa  '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('O maior valor digitado foi {}Kg'.format(maior))
print('O menor valor digitado foi {}Kg'.format(menor))
