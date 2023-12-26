from random import shuffle

p1 = input('Digite o nome de um aluno: ')
p2 = input('Digite o nome de um aluno: ')
p3 = input('Digite o nome de um aluno: ')
p4 = input('Digite o nome de um aluno: ')

# Coloque os nomes dos alunos em uma lista
alunos = [p1, p2, p3, p4]

# Embaralhe a ordem dos alunos
shuffle(alunos)

# Exiba a ordem de apresentação
print('A ordem de apresentação será:', alunos)
