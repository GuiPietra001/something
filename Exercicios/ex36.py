import locale

# Define a formatação local para o Brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

casa = float(input('Qual o preço da casa: '))
salario = float(input('Qual seu salário: '))
anos = int(input('Quantos anos de financiamento:'))
prestacao = casa / (anos * 12)  # preço da casa dividido por quantos meses ele vai pagar
minimo = salario * 30 / 100

# Formatação do valor da prestação usando a localidade brasileira
prestacao_formatada = locale.currency(prestacao, grouping=True)

print('Para pagar uma casa de {} Em {} anos você precisará pagar {}.'.format(locale.currency(casa, grouping=True), anos, prestacao_formatada), end='')
if prestacao <= minimo:
    print('EMPRÉSTIMO CONCEDIDO')
else:
    print('EMPRÉSTIMO NÃO PODE SER CONCEDIDO')
