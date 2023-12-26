n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

s = n1 + n2
d = n1 / n2
m = n1 * n2
di = n1 // n2
e = n1 ** n2

resultado = (
    "A soma é {},  a divisão é {}, a multiplicação é {}, "
    "a divisão inteira é {}, a potência é {:.5f}"
).format(s, d, m, di, e)

print(resultado)
