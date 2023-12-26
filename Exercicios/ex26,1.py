nome = str(input('Digite uma frase: '))

p1 = nome[0]  # Qual posição da primeira letra
qvalp = nome.lower().count(p1.lower())  # Quantas vezes a letra apareceu
ppl = nome.lower().index(p1.lower())  # Primeira posição da letra
upl = nome.lower().rindex(p1.lower())  # Última posição da letra

# Organiza os resultados em uma única string
resultado = (
    f"A letra {p1} aparece {qvalp} vezes\n"
    f"A primeira letra {p1} apareceu na posição {ppl}\n"
    f"A última letra {p1} apareceu na posição {upl}"
)

# Exibe a string organizada
print(resultado)
