"""
Closure e funções que retornam outras funções

introduction programação funcional
"""

def criar_salude(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

retorna_bom_dia = criar_salude('Bom dia')
retorna_boa_noite = criar_salude('Boa noite')

for nome in ['Caio', 'Cecília', 'Isadora']:
    print(retorna_bom_dia(nome))
    print(retorna_boa_noite(nome))