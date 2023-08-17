""" while/else """
""" Recurso específico de Py """

string = 'Valorqualquer'

i = 0

while i < len(string):
    letra = string[i]

    if letra in ' ':
        break

    print(letra)
    i += 1

else:
    print('Não encontrei um espacço na string!')
print('Fora do while.')

