velPERMITIDA = 80

med = float(input("Qual é a velocidade atual do carro? "))

if med <= velPERMITIDA:
    print("Tudo ok")
else:
    MN = 60
    MTADD = 7
    frt = MN
    while med > velPERMITIDA:
        frt += MTADD
        med -= 1
    print(
        "Você ultrapassou o limite de velocidade, sua multa será de {:.2f}R$".format(frt))
