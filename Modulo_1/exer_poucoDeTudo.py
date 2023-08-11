"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
##########################################################MANEIRA QUE EU RESOLVI O PROBLEMA##########################################################
# numero_digitado_usuario = input('Digite um número: ')

# try:
#     if int(numero_digitado_usuario) % 2 == 0:
#         print('Seu número é par!')
#     else:
#         print('Seu número é impar!')
# except:
#     print('Digite um número inteiro!')       

##########################################################MANEIRA QUE O PROF RESOLVEU##########################################################
# entrada = input('Digite um número: ')

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'O número {entrada_int} é {par_impar_texto}')
# else:
#     print('Você não digitou um número inteiro') 

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
##########################################################MANEIRA QUE EU RESOLVI O PROBLEMA##########################################################
# hora = input('Digite que horas são agora.(Exemplo: 13.45): ')

# try:
#     hora_convertida = float(hora)

#     if hora_convertida >= 0 and hora_convertida <= 11:
#         print('Bom dia!')
#     elif hora_convertida >= 12 and hora_convertida <= 17:
#         print('Boa tarde!')
#     elif hora_convertida >= 18 and hora_convertida < 24:
#         print('Boa noite!')
#     else:
#         print('Você sabe que digitou uma hora que não existe né? Me ajuda a te ajudar...(lembrando que 24 = 00 cara, use sua mente!)')

# except:
#     print('Digite uma hora válida, lembre-se do exemplo que te dei!') 

##########################################################MANEIRA QUE O PROF RESOLVEU##########################################################
#IGUAL EU
    
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
##########################################################MANEIRA QUE EU RESOLVI O PROBLEMA##########################################################
# nome = input('Digie seu prmeiro nome: ')

# if ' ' not in nome:
#     if len(nome) <= 4:
#         print('Seu nome é curto!')
#     elif len(nome) == 5 or len(nome) == 6:
#         print('Seu nome é normal!')
#     elif len(nome) > 6:
#         print('Seu nome é muito grande!')
# else:
#     print('Digite somente seu primeiro nome:')

##########################################################MANEIRA QUE O PROF RESOLVEU##########################################################

# nome = input('Digite seu nome: ')
# tamanho_nome = len(nome)

# if tamanho_nome > 1:        # VALIDANDO DADOS
#     if tamanho_nome <= 4:
#         print('Seu nome é curto')
#     elif tamanho_nome >= 5 and tamanho_nome <= 6:
#         print('Seu nome é normal')
#     else:
#         print('Seu nome é muito grande')
# else:
#     print('Digite mais de uma letra.')
