'''casa = float(input('Valor da casa: '))
salario = float(input('Salário: '))
anos = int(input('Anos de finança: '))
prestação = casa / (anos * 12)
minimo =  (salario * 30 / 100)
print('Para comprar uma casa de R${:.2f} em {} anos você pagará {:2f}'.format(casa, anos, prestação))
if prestação <= minimo:
    print('Emprestimo pode ser concedido')
else:
    print('Valor não pode ser concedido')'''
casa = float(input('Valor da casa: '))
salario = float(input('Seu salario: '))
anos = int(input('Anos de financiamento: '))
prestação = casa / (anos * 12)
minimo = (salario * 30 / 100)
print('Para pagar uma casa de R${:.2f} em {} anos você pagará R${:.2f}'.format(casa, anos, prestação))
if prestação <= minimo:
        print('Emprestimo pode ser concebido')
else:
    print('Emprestimo não pode ser concebido')