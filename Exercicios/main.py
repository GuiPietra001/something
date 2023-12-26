len(frase): Retorna o comprimento da string frase, ou seja, o número de caracteres.
frase.count('o'): Conta o número de ocorrências do caractere 'o' na string frase.
frase.count('o', 0, 13): Conta o número de ocorrências do caractere 'o' na substring de frase que vai do índice 0 ao índice 12 (13 não está incluso).
frase.find(deo): Este código contém um erro. Parece que você está tentando encontrar a posição da substring 'deo' na string frase. No entanto, você precisa colocar 'deo' entre aspas simples ou duplas para que seja tratado como uma string. Corrigindo para frase.find('deo'), isso retornaria o índice da primeira ocorrência da substring 'deo' em frase, ou -1 se não for encontrada.
'curso' in frase: Verifica se a substring 'curso' está presente em frase e retorna True se estiver, False caso contrário.
frase.replace('python', 'android'): Substitui todas as ocorrências da palavra 'python' por 'android' na string frase.
frase.upper(): Converte todos os caracteres em frase para maiúsculas.
frase.lower(): Converte todos os caracteres em frase para minúsculas.
frase.capitalize(): Converte a primeira letra da string frase para maiúscula e o restante para minúsculas.
frase.title(): Converte a primeira letra de cada palavra em frase para maiúscula.
frase.strip(): Remove espaços em branco no início e no final da string frase.
frase.rstrip(): Remove espaços em branco no final da string frase.
frase.lstrip(): Remove espaços em branco no início da string frase.
frase.split(): Divide a string frase em uma lista de substrings, utilizando espaços como delimitadores. Se nenhum argumento for fornecido para o método split(), ele considerará espaços em branco como o delimitador padrão.
' '.join(frase): Junta os elementos da lista (ou caracteres da string) frase, separando-os por espaços. O método join() é aplicado a uma string vazia com um espaço entre as aspas, indicando que você deseja juntar os elementos com espaços.





