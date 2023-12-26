larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = larg * alt 
tinta = área / 2

print('Sua parede tem a dimensão de {} x {} e a sua área é de {}m², você vai precisar de {}l de tinta.'.format(larg, alt, área, tinta))
