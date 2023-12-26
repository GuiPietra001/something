a = input('Qual o valor de: ')

resultado = (

    "Qual o formato? {}\n"
    "É número? {}\n"
    "É alfabeto? {}\n"
    "É alfanumérico? {}\n"
    "É maiusculo? {}\n"
    "É minusculo? {}\n"
    "É capitalizada? {}\n"
    "Tem espaço? {}"

).format(
    type(a),
    a.isnumeric(),
    a.isalpha(),
    a.isalnum(),
    a.isupper(),
    a.islower(),
    a.istitle(),
    a.isspace(),
)
print(resultado)
