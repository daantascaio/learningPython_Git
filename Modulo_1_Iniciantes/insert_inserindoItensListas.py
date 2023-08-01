"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

#        0   1   2   3     <-- Indices
lista = [10, 20, 30, 40]
print(lista)

lista.append('Caio')
print(lista)

del lista[-1]
print(lista)

lista.clear()
print(lista)

lista = [10, 20, 30, 40]
print(lista)

# Adicionado itens na lista usando o method insert, ele recebe dois argumentos: 1ª o indice onde eu vou alocar o meu iten; 2ª o iten que vai ser adicionado na minha lista
lista.insert(1, 15)
print(lista)

# Tentando acessar algum indice que não existe na minha lista, eu recebo o erro -- IndexError --



