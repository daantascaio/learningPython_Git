
import pprint

def p(v):
    pprint.pprint(v)

# lista = [n for n in range(10) if n < 5]

# print(lista)

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]


novos_produtos = [
    {**novo_produto, 'preco': novo_produto['preco'] * 1.05}
    if novo_produto['preco'] > 20 else {**novo_produto}
    for novo_produto in produtos
    if (novo_produto ['preco'] >= 20 and novo_produto ['preco'] * 1.05) > 10
]

p(novos_produtos)