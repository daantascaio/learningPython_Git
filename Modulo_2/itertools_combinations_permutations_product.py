# Combination, Permutations and Produc1t -  Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product



def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()





people = [
    'João', 'Maria', 'Caio', 'Camila'
]

camisetas = [
    ['Preta', 'Branca'],
    ['P', 'G', 'GG', 'XGG'],
    ['Masculino', 'Feminino', 'Infantil'],
    ['Algodão', 'Dri-Fit']
]

# print('Combinations')
# print_iter(combinations(people, 2))

# print('Permutations')
# print_iter(permutations(people, 2))

print('Product')
print_iter(product(*camisetas))

