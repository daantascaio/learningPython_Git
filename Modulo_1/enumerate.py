"""
enumerate --> enumera iteráveis (índices)
"""
lista = ['Maria', 'João', 'Caio']
lista.append('Rodrigo')

lista_enumerada = enumerate(lista)


# for i in lista_enumerada:
#     print(i)

for indice, nome in lista_enumerada:
    print(indice, nome)

# for i in enumerate(lista):
#     indice, nome = i
#     print(indice, nome)

# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')