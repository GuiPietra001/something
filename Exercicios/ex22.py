nome = input('Digite seu nome para análise: ')

maius = nome.upper()
minus = nome.lower()
iat = len(nome)
las = nome.replace(" ", "")  # Remove os espaços
pest = len(las)
separa = nome.split()
print('Seu nome em maiúsculo é {}'.format(maius))
print('Seu nome em minúsculo é {}'.format(minus))
print('Seu nome tem {} letras'.format(pest))
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))
