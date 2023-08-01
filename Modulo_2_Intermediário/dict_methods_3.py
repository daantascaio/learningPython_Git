"""
# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves             
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe


copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - Apaga um item com a chave especificada (del)
popitem - Apaga o último item adicionado
update - Atualiza um dicionário com outro
"""

p1 = {
    'nome': 'Caio',
    'sobrenome': 'Dantas',
}

# print(p1['nome'])
# print(p1.get('nome', 'Não existe')) # Se nome não existir eu vou exibir 'Não exite'

# nome = p1.pop('nome')
# print(nome)
# print(p1)

# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)


# 1º Forma de escrever update
print(p1)
p1.update({
    'age': 1,
    'nome': 'Cecília',
}
)
print(p1)

# 2º Forma de escrever update
p1.update(nome='Cecília', age=1)

# 3º Forma de escrever update
tupla = ('nome', 'novo_valor'), ('idade', 30) # Pode ser list também
p1.update(tupla)
print(p1)