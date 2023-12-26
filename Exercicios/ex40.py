nota1 = float(input('Valor da primeira nota:'))
nota2 = float(input('Valor da segunda nota: '))
media = (nota1 + nota2) / 2
if 5 >= media and media < 7:
    print('Aluno está em recuperação!')
elif media < 5:
    print('O aluno está REPROVADO')
else:
    print('O aluno está em APROVADO')