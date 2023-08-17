# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos


dataSet = {1, 2, 3}
dataSet_2 = {2, 3, 4}

dataSet_3 = dataSet | dataSet_2
print(dataSet_3)

dataSet_3 = dataSet & dataSet_2
print(dataSet_3)

dataSet_3 = dataSet - dataSet_2
print(dataSet_3)

dataSet_3 = dataSet_2 - dataSet
print(dataSet_3)