a = input('Qual é o valor de: ')

resultado = (
    "Qual a classe? {}\n"
    "É numerico? {}\n"
    "É alfabeto? {}\n"
    "É alfanúmerico? {}\n"
    "É maiusculas? {}\n"
    "É minusculas? {}\n"
    "É capitalizada? {}"
).format(
    type(a),
    a.isnumeric(),
    a.isalpha(),
    a.isalnum(),
    a.isupper(),
    a.islower(),
    a.istitle()
)

print(resultado)
