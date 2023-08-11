# Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis
# Mutáveis [] {} set()
# Imutáveis () "" 0 0.0 None False range(0, 10)
lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ''
inteito = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)


def mostra_falsy(valor):
    return 'falsy'if not valor else 'truthy'


print(f'TESTE', mostra_falsy('TESTE'))
print(f'{lista=}', mostra_falsy(lista))
print(f'{dicionario=}', mostra_falsy(dicionario))
print(f'{conjunto=}', mostra_falsy(conjunto))
print(f'{tupla=}', mostra_falsy(tupla))
print(f'{string=}', mostra_falsy(string))
print(f'{inteito=}', mostra_falsy(inteito))
print(f'{flutuante=}', mostra_falsy(flutuante))
print(f'{nada=}', mostra_falsy(nada))
print(f'{falso=}', mostra_falsy(falso))
print(f'{intervalo=}', mostra_falsy(intervalo))