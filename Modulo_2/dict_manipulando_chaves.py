"""
Manipulando chaves e valores em dicionários
"""
pessoa = { 
    'nome': 'Caio',
    'sobrenome': 'Dantas',
    'idade': 20,
    'altura': 1.83,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}


pessoa['peso'] = 105
print(pessoa['peso'])
print(pessoa)

del pessoa['peso']
print(pessoa)

if pessoa.get('peso') is None:
    print('Ahu')

else:
    print(pessoa)