# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))
import pprint

def p(v):
    pprint.pprint(v)


lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

lista = [
    numero * 2
    for numero in range(10)
]
# print(list(range(10)))
# print(lista)

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
novos_produtos = [
    {**novo_produto, 'preco': novo_produto['preco'] * 1.05}
    if novo_produto['preco'] > 20 else {**novo_produto}
    for novo_produto in produtos
]

# print(novos_produtos)
# print(*novos_produtos, sep='\n')
# p(novos_produtos)