from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0

for pess in range(1, 8):
    nasc = int(input('Em que ano nasceu a {}º pessoa    '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
else:
    totmenor += 1
print('Ao total tivemos {} pessoas maiores'.format(totmaior))
print('Ao total tivemos {} pessoas menor'.format(totmenor))
