num = int(input('Digite um valor: '))
tot = 0

for c in range(1, num, +1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\[O número {} foi divisivel {} vezes'.format(num, tot))
if tot == 2:
    print('Por isso ele é primo')
else:
    print('Por isso não é primo')
