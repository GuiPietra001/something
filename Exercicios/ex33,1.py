primeiroValor = int(input('Qual o primeiro valor? '))
segundoValor = int(input('Qual o segundo valor? '))
terceiroValor = int(input('Qual o terceiro valor? '))

menor_valor = primeiroValor

if segundoValor < menor_valor:
    menor_valor = segundoValor

if terceiroValor < menor_valor:
    menor_valor = terceiroValor

print('O menor valor é {}'.format(menor_valor))

maior_valor = primeiroValor

if segundoValor > maior_valor:
    maior_valor = segundoValor
    
if terceiroValor > menor_valor:
    maior_valor = terceiroValor
print('O maior valor é {}'.format(maior_valor))