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

cities = ['Salvador', 'Ubatuba', 'Belo Horizonte']
abbreviated_states = ['BA', 'SP', 'MG', 'RJ']


def function_zipper(small_list, big_list):

    cont = []
    for i in zip(small_list, big_list):
        i = tuple(i)
        cont.append(i)
    return print(cont)

function_zipper (cities, abbreviated_states)