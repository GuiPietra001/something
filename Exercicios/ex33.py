fristValor = int(input('Digite o primeiro valor: '))
seconValor = int(input('Digite o segundo valor: '))
thirdValor = int(input('Digite o terceiro valor: '))

# Encontrar o maior valor
if fristValor > seconValor and fristValor > thirdValor:
    maior_valor = fristValor
elif seconValor > fristValor and seconValor > thirdValor:
    maior_valor = seconValor
else:
    maior_valor = thirdValor

# Exibir o maior valor
print('O maior valor é {}'.format(maior_valor))

# Encontrar o menor valor
if fristValor < seconValor and fristValor < thirdValor:
    menor_valor = fristValor
elif seconValor < fristValor and seconValor < thirdValor:
    menor_valor = seconValor
else:
    menor_valor = thirdValor

# Exibir o menor valor
print('O menor valor é {}'.format(menor_valor))
