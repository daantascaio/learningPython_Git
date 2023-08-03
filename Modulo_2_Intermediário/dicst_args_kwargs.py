# Empacotamento e desempacotamento de dicionários

# a, b = 1, 2
# a, b = b, a

pessoa = { 
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'age': 16,
    'altura': 1.70,
}

pessoa_completa = {**pessoa, **dados_pessoa}
print(pessoa_completa)
# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2, b1, b2)

# print()

# for chave, valor in pessoa.items():
#     print(chave, valor)


# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS', args)

    for chave, valor in kwargs.items(): 
        print(chave, valor)

# mostro_argumentos_nomeados(1, 2, 3, 4, nome='Joana', idade=12)
# mostro_argumentos_nomeados(**pessoa_completa)


configuracoes = {
    'arg': 1,
    'arg1': 3,
    'arg2': 7,
    'arg3': 6,
    'arg4': 5,
}

mostro_argumentos_nomeados(**configuracoes)