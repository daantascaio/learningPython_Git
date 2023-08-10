import copy
import os

# copy, sorted, produtos.sort
# Exercícios

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

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

# def values_second_index_dictionaries(product_list):
#     for dictionary in product_list:
#         yield dictionary['preco']

# def increase_10_percent(numbers):
#     result = []
#     for num in numbers:
#         num = num * 1.1
#         num = "{:.2f}".format(num)
#         result.append(float(num))
#     return result

# def check_price():

#     while True:
#         price = input("Digite o preço do produto: ")

#         try:
#             price = float(price)
          
#         except ValueError:
#             print("Preço inválido. Digite um preço correto!")
#             continue

#         return price

# def create_products(name_product, price_product):

#     product_dict = {'nome': name_product, 'preco': price_product}

#     return product_dict

# values_without_increase = list(values_second_index_dictionaries(produtos))
# print(f'VALOR ORIGINAL: {values_without_increase}')

# values_whith_increase = list(increase_10_percent(values_without_increase))
# print(f'VALUE WITH INCREASE 10%: {values_whith_increase}')



# while True:
#     cat = input('Digite [i] para adicionar produtos na lista ou não digite nada para parar o sistema: ')

#     if cat == 'i':

#         name_product = input('Digite o nome do produto: ')
#         price_product = check_price()
        
#         new_product = create_products(name_product, price_product)

#         products_copy = copy.deepcopy(produtos)

#         products_copy.append(new_product)
#         print(products_copy)
#         continue
#     os.system('cls')
#     break

# print(f'\nLISTA ORIGINAL')


# for i in produtos:
#     nome = i['nome']
#     preco = i['preco']
#     print(f"Nome: {nome}, Preço: {preco}")

# print(f'\nLISTA DEEPCOPY')

# for i in products_copy:
#     nome = i['nome']
#     preco = i['preco']
#     print(f"Nome: {nome}, Preço: {preco}")


# s = input('\nPressione a tecla [Enter] para continuar! ')
# os.system('cls')
"""
2) Ordene os produtos por nome decrescente (do maior para menor)
   Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
"""


print(produtos.sort)










"""
3) Ordene os produtos por preco crescente (do menor para maior)
   Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
"""

