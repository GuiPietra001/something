num = int(input('Digite um número inteiro: '))
print('''[ 1 ] Digite para Binário
 [ 2 ] Digite para Octal
 [ 3 ] Digite para Hexadecimal''')
n1 = int(input('Digite seu valor: '))
if n1 == 1:
    print('Seu numero {} Em Binário é {}'.format(num, bin(num) [2:]))
elif n1 == 2:
    print('Seu numero {} Em octal é {}'.format(num, oct(num) [2:]))
elif n1 == 3:
    print('Seu numero {} Em Hexadecimal é {}'.format(num, oct(num) [2:] ))
else:
    print('Digite um número válido.')