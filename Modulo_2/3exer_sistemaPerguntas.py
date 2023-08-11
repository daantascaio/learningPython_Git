# Exercício - sistema de perguntas e respostas
import os

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
    

def separe_optionsInlines(i0):
    if i0 == 0: 
        i0 = separetes_indicesDicts_In_var(0)
        organizing_options = i0['Opções']
        for keys_or, values_or in enumerate(organizing_options, start=1):
            options_organized_question1 = print(f'{keys_or}) {values_or}')
        return options_organized_question1
        
    elif i0 == 1:  
        i0 = separetes_indicesDicts_In_var(1)
        organizing_options = i0['Opções']
        for keys_or, values_or in enumerate(organizing_options, start=1):
            options_organized_question2 = print(f'{keys_or}) {values_or}')
        return options_organized_question2

    elif i0 == 2:
        i0 = separetes_indicesDicts_In_var(2)
        organizing_options = i0['Opções']
        for keys_or, values_or in enumerate(organizing_options, start=1):
            options_organized_question3 = print(f'{keys_or}) {values_or}')
        return options_organized_question3
    
    else:
        print('Erro desconhecido')
        return None


def obtem_trata_resp ():
    
    while True:
        resposta = input('Escolha uma alternativa correta: ')
        if len(resposta) == 1:
            
            if resposta == '1' or resposta == '2' or resposta == '3' or resposta == '4':
                return resposta
            else:
                print('Escolha uma alternativa que exista!') 

        else:
            print('Escolha apenas 1 alternativa! ')

        
            

while True:
    
    choices_users = input('Digite [I] para inicar a prova ou digite [P] sair da prova: ')

    if choices_users.upper().strip() == 'I':
        os.system('cls')
        cont = 0
        print('\tBoa sorte!\n')
        first_question = separetes_indicesDicts_In_var(0)
        print(f'Pergunta: {first_question["Pergunta"]}\n')

        separe_optionsInlines(0)
        obtem_resp = obtem_trata_resp()

        if obtem_resp == '1':
            print('Você errou!')
            

        elif obtem_resp == '2':
            print('Você errou!')
            

        elif obtem_resp == '3':
            print('Você acertou! 🎉')
            cont += 1

        elif obtem_resp == '4':
            print('Você errou!')

        

        second_question = separetes_indicesDicts_In_var(1)
        print(f'Pergunta: {second_question["Pergunta"]}\n')

        separe_optionsInlines(1)
        obtem_resp = obtem_trata_resp()

        if obtem_resp == '1':
            print('Você acertou! 🎉')
            cont += 1

        elif obtem_resp == '2':
            print('Você errou!')
            

        elif obtem_resp == '3':
            print('Você errou!')
            

        elif obtem_resp == '4':
            print('Você errou!')

        

        third_question = separetes_indicesDicts_In_var(2)
        print(f'Pergunta: {third_question["Pergunta"]}\n')

        separe_optionsInlines(2)
        obtem_resp = obtem_trata_resp()

        if obtem_resp == '1':
            print('Você errou!')
            

        elif obtem_resp == '2':
            print('Você acertou! 🎉')
            cont += 1

        elif obtem_resp == '3':
            print('Você errou!')
            

        elif obtem_resp == '4':
            print('Você errou!')

        print(f'/n Você acertou {cont} de 3 perguntas \n')
        
    elif choices_users.upper().strip() == 'P':
        os.system('cls')

        break
        
    else:
        print('Stop being a stupid user, write a correct character!')

    

## Resolução professor




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

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')


    

