peso1 = float(input('DIGITE SEU PESO: '))
altura1 = float(input('DIGITE SUA ALTURA: '))
ivc = peso1 / (altura1 * altura1)
ipc = peso1 / (altura1 * altura1)
imc = ipc
if imc > 17 and imc <= 18.4:
    print('ABAIXO DO PESO')
elif imc >= 18.5 and imc <= 24.9:
    print('PESO NORMAL')
elif imc >= 25 and imc <= 29.9:
    print('ACIMA DO PESO')
elif imc >= 30 and imc <= 34.9:
    print('OBESIDADE GRAU 1')
elif imc >= 35 and imc <= 40:
    print('OBESIDADE GRAU 2')
elif imc > 40:
    print('OBESIDADE GRAU 3 PROCURE UM MÉDICO!')
   




