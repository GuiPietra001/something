velocidade = float(input('Qual a velocidade atual do carro: '))
if velocidade > 80:
    print('[MULTADO!] você excedeu o limite de velocidade permitida que é de 80km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de {}'.format(multa))    
print('dirija com segurança!')
    