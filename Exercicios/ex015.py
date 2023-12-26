car = float(input('Quantos km você percorreu: '))
dia = float(input('Quantos dias você ficou com o carro: '))

custo_km = car * 0.15  # Custo baseado na distância percorrida

# Aqui você pode adicionar uma lógica para calcular o custo com base nos dias
custo_dia = dia * 60  # Substitua "alguma_taxa" pela taxa desejada

# Calcula o custo total
custo_total = custo_km + custo_dia

# Imprime os resultados
print('Você andou {} Km e ficou {} dias com o carro, o custo total é {:.2f}'.format(
    car, dia, custo_total))
