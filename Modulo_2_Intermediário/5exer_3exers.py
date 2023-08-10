# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

"""
1) Aumente os preços dos produtos a seguir em 10%
   Gere novos_produtos por deep copy (cópia profunda)
"""
# SE FORMOS PENSAR EM LARGA ESCOLA, ACHO QUE ESSA MANEIRA VAI GASTAR MUITO PODER DE PROCESSAMEMTO
# novos_precos = [var_temporaria['preco'] for var_temporaria in produtos]

# print(novos_precos)

# def aumenta_10porcento(lista_de_numeros):
#     numeros_aumentados = []
#     for num in lista_de_numeros:
#         numeros_aumentados.append(num * 1.10)
#     return numeros_aumentados

# print(aumenta_10porcento(novos_precos))

# for i in produtos:
#     preco_alterado = i['preco']
#     print(preco_alterado)

def values_second_index_dictionaries(product_list):
    for dictionary in product_list:
        yield dictionary['preco']

def increase_10_percent(numbers):
    result = []
    for num in numbers:
        num = num * 1.1
        num = "{:.2f}".format(num)
        result.append(float(num))
    yield list(result)

values_without_increase = list(values_second_index_dictionaries(produtos))
print(f'VALOR ORIGINAL: {values_without_increase}')

values_whith_increase = increase_10_percent(values_without_increase)
print(f'VALUE WITH INCREASE 10%: {values_whith_increase}')





