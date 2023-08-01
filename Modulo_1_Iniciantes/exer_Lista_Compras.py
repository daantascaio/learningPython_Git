"""
Faça uma lista de compras com list
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista
"""

print('Bem vindo ao compras online!\n')

import os

lista_compras = []

while True:

    print('Selecione uma opção:')
    inserir_apagar_listar = input('[i]nserir [a]pagar [l]istar: ' ).lower()

    if len(inserir_apagar_listar) > 1:
        os.system('cls')
        print(f'Digite o valor dentro dos [], se referindo à ação que deseja realizar!\n')
        continue

    if inserir_apagar_listar == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista_compras.append(valor)

        for indice, nome in enumerate(lista_compras):
            print(f'\n \t{indice} {nome}\n')
        continue

    elif inserir_apagar_listar == 'a':
        os.system('cls')
        apagar_indice = input('Escolha um índice para apagar: ')
        
        try:
            apagar_indice_int = int(apagar_indice)

            try:
                del lista_compras[apagar_indice_int]
                                                                        
                for indice, nome in enumerate(lista_compras):                   # NESSE try, OLHAR O EXEMPLO DO PROFESSOR! FOI MUITO MELHOR TRABALHADO
                    print(f'\n \t{indice} {nome}\n')

            except IndexError:
                print(f'Esse índice não existe!\n')
             

        except ValueError:
            print(f'Não foi possível apagar esse índice!\n')

    elif inserir_apagar_listar == 'l':
        os.system('cls')
        if lista_compras == []:
            print(f'Não existe uma lista para ser listada!\n')

        for indice, nome in enumerate(lista_compras):
            print(f'\n \t{indice} {nome}\n')

    else:
        os.system('cls')
        print('Digita o valor correto cara!')

    # break   



#################################### SOLUÇÃO PROFESSOR ####################################

import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')
        

    

    
        
        

    

    

    