"""
Exercício

Crie funções que duplicam, triplicam e quadruplicam 
o número recebido como parâmetro
"""

import random

# def duplica_numero(number):
#     return number * 2

# def triplica_numero(number):
#     return number * 3

# def quadruplica_numero(number):
#     return number * 4

def create_function_multiplica(number):
    def action_multiplica(multiplicado=num):
        return multiplicado * number
    return action_multiplica

def aleatory_number(N):
    N = random.getrandbits(14)
    return N

num = aleatory_number(random)
retorna_multiplicacao = create_function_multiplica(num)


print(f'Esse é o número gerado: {num}')


print(f'Número duplicado: {retorna_multiplicacao(2)}\nNúmero triplicado: {retorna_multiplicacao(3)}\nNúmero quadruplicado: {retorna_multiplicacao(4)}')
# print(f'Número duplicado: {duplica_numero(num)}\nNúmero triplicado: {triplica_numero(num)}\nNúmero quadruplicado: {quadruplica_numero(num)}')