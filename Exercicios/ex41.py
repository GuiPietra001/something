from datetime import date
clas = int(input('Digite seu ano de nascimento: '))
atual = date.today().year
idade = atual - clas
if idade <= 9:
    print('Atleta Mirim')
elif idade >= 9 and idade < 14:
    print('O atleta é Infantil!')
elif idade > 14 and idade < 19:
    print('Atleta Junior')
elif idade >= 19 and idade < 25:
    print('Atleta Sênior')
else:
    print('Atleta Master')