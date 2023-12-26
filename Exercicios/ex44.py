# Solicita o preço dos produtos ao usuário
preço = float(input('Qual o preço dos produtos? '))

# Apresenta as opções de forma de pagamento
print(''' Formas de pagamento:
[ 1 ] À vista em dinheiro/cheque   
[ 2 ] À vista no cartão
[ 3 ] Parcelado em 2x no cartão
[ 4 ] Parcelado em 3x ou mais no cartão  
''')

# Solicita a forma de pagamento escolhida
opção = int(input('Qual a forma de pagamento? '))

# Verifica a opção escolhida e calcula o total a ser pago
if opção == 1:
    total = preço - (preço * 10 / 100)  # Desconto de 10% para pagamento à vista em dinheiro/cheque
elif opção == 2:
    total = preço - (preço * 5 / 100)  # Desconto de 5% para pagamento à vista no cartão
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de {}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)  # Acréscimo de 20% para pagamento parcelado em 3x ou mais
    totaldeparcelas = int(input('Quantas parcelas? '))
    parcela = total / totaldeparcelas
    print('Sua compra será parcelada em {}x de R$ {:.2f} SEM JUROS!'.format(totaldeparcelas, parcela))
else:
    total = 0
    print('Opção inválida de pagamento')
# Exibe o total a ser pago
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final'.format(preço, total))
