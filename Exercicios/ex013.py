salário = float(input('Qual é o salário do funcionária?   R$'))

aumento = salário + (salário * 15 / 100)

print('Um funcionário que ganhava R${}, com 15%, de aumento, pa ssa a receber R${:.2f}'.format(salário, aumento))