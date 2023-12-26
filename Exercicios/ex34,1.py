salario = float(input('Qual seu salário: '))

if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${} Começará a ganhar R${}'.format(salario, novo))
