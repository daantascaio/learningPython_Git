"""

Escreva um programa que imprima os números pares de 1 a 50.

"""
# Eu
for numero in range(1, 51):
    
    if numero % 2 == 0:
        print(numero)
    


# ChatGPT

for numero in range(1, 51):
    if numero % 2 == 0:
        print(numero)

# Explicação:

#     O for percorre a sequência de números de 1 a 50 (novamente, o segundo parâmetro do range não está incluso).
#     Em cada iteração do loop, verificamos se o número atual (numero) é par usando o operador de módulo %. Se numero % 2 for igual a 0, isso significa que o número é par.
#     Se o número for par, ele é impresso na tela.

# Ao executar esse código, você verá a saída que mostra todos os números pares de 1 a 50, um em cada linha.

