
r = float(input('Quanto dinheiro você tem: '))
usd_rate = 4.92
btc_rate = 209830.46
eur_rate = 5.40
ars_rate = 0.0061

print(f'''
    {r} convertido em Dólares é: {r / usd_rate:.2f} USD
    {r} convertido em Bitcoin é: {r / btc_rate:.8f} BTC
    {r} convertido em Euros é: {r / eur_rate:.2f} EUR
    {r} convertido em Peso Argentino é: {r / ars_rate:.2f} ARS 
''')