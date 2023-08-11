# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

si = {1, 2, 3, 4, 5, 4, 4, 5, 6, 6, 6, 7} 
print(si)   # repare que no print ele retirou os valores duplicados

lista = [ 1,2,3,4,5,6,7,8,9,3,3,3,3,2,2,2,2,1,1,1,3,4,5,6,5464,35,345,345,345,345,345,345,345,345,345,345,]
s1 = set(lista)
 
lista2 = list(s1)   
print(lista2)   # agora a minha lista não tem os números repetidos


# dataSet = {1, 2, 3, [ '23', 123, True ]}

# print(dataSet) # Isso gera um TypeError
