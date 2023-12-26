import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjecente: '))
catop = co ** 2
catad = ca ** 2
hipotenusa = math.sqrt(catop + catad)

print('O valor da hipotenusa é {:.2f}'.format(hipotenusa))

