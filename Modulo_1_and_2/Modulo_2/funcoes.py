"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""

# def imprimir(a, b, c):
#     print('Caio')
#     print('Caio')
#     print('Caio')
#     print('Caio')
#     print('Caio')
#     print('Caio')

# imprimir(1, 2, 3)


def saudacao(nome):
    print(f'Olá, {nome}')


saudacao('Caio')
saudacao('Gabi')