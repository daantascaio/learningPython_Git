"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
# Lista original
lista =[10, 20, 30, 40]
print(lista)

# Usando o method del
del lista[2] 
print(lista)

# Adicionando itens na minha lista usando o method append
lista.append(50)
lista.append(60)
lista.append(70)
print(lista)

# Usando o method pop para remover o ULTIMO iten da minha lista
lista.pop()
print(lista)
# Mas, se eu específicar o índice do item, posso remover ele também
item_removido = lista.pop(0)
print(lista, 'Removido' , item_removido)


