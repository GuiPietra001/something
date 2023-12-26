nome = str(input('Digite uma frase: '))

p1 = nome[0] #Qual posição da primeira letra
qvalp = nome.lower().count(p1.lower())  #Quantas vezes a letra apareceu
ppl = nome.lower().index(p1.lower())   #Primeira posição da letra
upl = nome.lower().rindex(p1.lower()) #ultima posição da letra


print('A letra {} aparece {} vezes'.format(p1, qvalp))
print('A primeira letra {} apareceu na posição {}'.format(p1, ppl))
print('A última letra {} apareceu na posição {}'.format(nome, upl ))