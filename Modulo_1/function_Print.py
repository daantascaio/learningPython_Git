'''
Print() é usado para exibir algo na tela.

A function recebe Argumentos
'''

print(1) # Observe que o Argumento dessa print é 1

print(1, 2, 3) # Usando a - , -  eu posso adicionar mais Argumentos para minha function

# Por padrão a function print separa seus argumentos com space 

print(1 ,2 , 34,  sep="-") # Usando o - sep="" - consigo usar outro tipo de separador, observe no exemplo 

print("----------------------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------------------------#

# \r\n -> CRLF = Quebra de linha
# \n -> LF
print(1, 2, 34, sep="-", end="&&")  #Esse é um exemplo sem utulizar a quebra de linha
print(1, 2, 34, sep="-", end="&&") 

print(1, 2, 34, sep="-", end=" && \n") # Usando a quebra de linha
print(1, 2, 34, sep="-", end=" && \n") #
print(1, 2, 34, sep="-", end=" && \n") #
# O Argumento nomenado - end=" " - nos da a possibilidade de mudar o final de linha, veja que os && ficaram no final dos argumentos inicias

