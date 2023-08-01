# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]


# create function that separates dicts into vars
# receber indice e separar os dicts
def separetes_indicesDicts_In_var(i):
    if i == 0:
        return perguntas[0]
    elif i == 1:
        return perguntas[1]
    elif i == 2:
        return perguntas[2]
    else:
        print('Erro desconhecido')
        return None

    


    

