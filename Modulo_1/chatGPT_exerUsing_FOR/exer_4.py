"""

Escreva um programa que imprima os números ímpares de 50 a 100.

"""

# Eu
for numero in range(50, 101):
    
    if numero % 2 != 0:
        print(numero)

# ChatGPT
for numero in range(51, 101, 2):
    print(numero)

#     Explicação:

#     O for percorre a sequência de números de 51 a 100 utilizando o range, com um passo de 2 (ou seja, pulando de 2 em 2).
#     Isso garante que apenas os números ímpares entre 51 e 100 serão considerados, já que começamos no 51 e adicionamos 2 em cada iteração.
#     Em cada iteração do loop, o número atual é impresso na tela.

# Ao executar esse código, você verá a saída que mostra todos os números ímpares de 50 a 100, um em cada linha.

