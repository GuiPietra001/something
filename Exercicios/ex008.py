m = float(input('Uma distância em metros: '))

dm = m * 10
cm = m * 100
mm = m * 1000
dam = m / 10
hm = m / 100
km = m / 1000

print('A medida de {} corresponde a \n {:.3f} Km \n a {:.2f} HM \n a {:.1f} DAM \n a {:.0f} DM \n a {:.0f} CM \n a {:.0f} MM \n'.format(m, km, hm, dam, dm, cm, mm))