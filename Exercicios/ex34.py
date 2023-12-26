salario = float(input('Digite seu salário: '))

if salario <= 1250:
    novo = salario + (salario * 0.15)
else:
    novo = salario + (salario * 0.10)

print('O seu salario é R${:.2f}'.format(novo))
