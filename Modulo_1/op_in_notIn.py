# Operadores in e not in
# Strings são interáveis
#  0 1 2 3  
#  C a i o
# -6-5-4-3
# nome = 'Caio'

# print(nome[3])
# print(nome[-2])
# print('aio' in nome)
# print('dan' in nome)
# print('io' not in nome)
# print('ios' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
        print(f'{encontrar} está em {nome}')
else:
        print(f'{encontrar} não está em {nome}')