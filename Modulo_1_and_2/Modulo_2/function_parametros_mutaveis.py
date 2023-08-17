# Problema dos parâmetros mutáveis em funções Python

def adiciona_cliestes(nome, lista=None):
    if lista is None:
        lista = []

    lista.append(nome)
    return lista



cliente1 = adiciona_cliestes('Caio')
adiciona_cliestes('João', cliente1)
adiciona_cliestes('Feranando', cliente1)
adiciona_cliestes('Julgo', cliente1)
print(cliente1)

cliente2 = adiciona_cliestes('Jojo')
adiciona_cliestes('Ronaldo', cliente2)
print(cliente2)