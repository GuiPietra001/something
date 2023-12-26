from random import choice

p1 = input('Digite o nome de um Aluno: ')
p2 = input('Digite o nome do segundo aluno: ')
p3 = input('Digite o nome do terceiro aluno: ')
p4 = input('Digite o nome do quarto aluno: ')
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
alunos = p1, p2, p3, p4
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
sorteio = choice(alunos)
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
print('O aluno sorteado é {}'.format(sorteio))
