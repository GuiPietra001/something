distancia = float(input('Qual é a distância de sua viagem? '))
print('Você está prestes a começar uma viagem de {} Km'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('O preço de sua passagem será {:.2f} R$'.format(preco))
