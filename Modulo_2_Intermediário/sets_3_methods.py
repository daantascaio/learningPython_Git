# Métodos úteis:
# add, update, clear, discard

dataSet = {1, 2}
print(dataSet)

dataSet.add(3)
print(dataSet)

dataSet.update('Caio')
print(dataSet) # perceba que o meu nome ficou iterado e todo desorganizado

dataSet.update(('Caio Dantas',))
print(dataSet)  # veja que para adicionar uma frase no meu set, eu usei uma tupla. 
                # Usando uma tupla os valores ficam na ordem que eu escrevo na tupla

# dataSet.clear()
# print(dataSet)

dataSet.discard('Caio Dantas')
print(dataSet)
dataSet.discard('a')
print(dataSet)
dataSet.discard('C') # C e c são diferentes
print(dataSet)
dataSet.discard('i')
print(dataSet)
dataSet.discard('o')
print(dataSet)







