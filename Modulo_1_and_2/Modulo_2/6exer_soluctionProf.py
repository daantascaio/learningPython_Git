# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

"""
cities = ['Salvador', 'Ubatuba', 'Belo Horizonte']
abbreviated_states = ['BA', 'SP', 'MG', 'RJ']


def function_zipper(small_list, big_list):
                                                                                        # I
    cont = []
    for i in zip(small_list, big_list):
        cont += i
    return print(cont)

function_zipper(cities, abbreviated_states)
"""


# # # def zipper(l1, l2):
# # #     intervalo = min(len(l1), len(l2))
# # #     return [(l1[i], l2[i]) for i in range(intervalo)]

from itertools import zip_longest

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(list(zip(l1, l2)))
print()

print(list(zip_longest(l1, l2, fillvalue='SEM CIDADE')))