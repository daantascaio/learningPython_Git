"""
Escreva um programa que imprima os múltiplos de 7 menores que 100 usando um loop "while".
"""


count = 0
while True:
    
    if count % 7 == 0:
        print(count)
    
    count += 1

    if count > 100:
        break

#ChatGPT

# Inicializa a variável para armazenar o múltiplo atual
multiplo = 0

# Imprime os múltiplos de 7 menores que 100 usando um loop while
while multiplo < 100:
    print(multiplo)
    multiplo += 7

"""
Explicação do código:

    O programa inicializa a variável multiplo com o valor zero antes do loop começar.
    O loop while continuará executando enquanto o valor de multiplo for menor que 100.
    Dentro do loop, o programa imprime o valor atual de multiplo.
    Em seguida, o valor de multiplo é incrementado em 7 para encontrar o próximo múltiplo de 7.
    O loop continua a imprimir os múltiplos de 7 menores que 100 até que o valor de multiplo seja maior ou igual a 100, momento em que o loop será encerrado.

Agora, o programa imprimirá todos os múltiplos de 7 menores que 100 usando um loop "while". Cada múltiplo será impresso em uma linha separada no console.
"""
