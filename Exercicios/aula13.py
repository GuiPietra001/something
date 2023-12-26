'''i = int(input('Digite o inicio: '))
f = int(input('Digite o fim:    '))
p = int(input('Digite o pass:   '))

for c in range(i, f+1, p):
    print(c)
print('fim')'''
s = 0
for c in range(0, 5):
    k = int(input('Digite um valor: '))
    s += k
print('O resultado da soma foi {}'.format(s))