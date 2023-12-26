print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
primeiro_segmento = float(input('Primeiro segmento: '))
segundo_segmento = float(input('Segundo segmento: '))
terceiro_segmento = float(input('Terceiro segmento: '))

# Verifica se é possível formar um triângulo
if (
    primeiro_segmento < segundo_segmento + terceiro_segmento and
    segundo_segmento < primeiro_segmento + terceiro_segmento and
    terceiro_segmento < primeiro_segmento + segundo_segmento
):
    print('Os segmentos acima podem formar um triângulo!')
else:
    print('Os segmentos acima não podem formar um triângulo!')
