"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

################### MANEIRA QUE EU RESOLVI O PROBLEMA ###################

# # Formatando o cpf de maneira simples e iniciante                       Uma outra maneira mais avançada é usando o method replace, veja o exemplo!
# cpf = '746.824.890-70'                                                  # cpf = "777.777.77-77"                                            
# cpf_formatado = ''
#                                                                         # Remove os pontos e o traço do CPF
# for num_cpf in cpf:                                                     # cpf_sem_pontos_e_traco = cpf.replace(".", "").replace("-", "")
#     if num_cpf.isdigit():                                           
#         cpf_formatado += num_cpf

# print(cpf_formatado)                                                  # print(cpf_sem_pontos_e_traco)  # Output: 7777777777                                          

# cpf_formatado_sem_os_ultimos_dois_digitos = cpf_formatado[:-2]
# num_multiplicador_cpf = 10
# resultado_multiplicacao_cpf = 0

# for i in cpf_formatado_sem_os_ultimos_dois_digitos:
#     i_int = int(i)
#     resultado_multiplicacao_cpf += i_int * num_multiplicador_cpf
#     num_multiplicador_cpf -= 1

# resultado_x10 = resultado_multiplicacao_cpf * 10

# print(resultado_x10)

# resultado_x10_divido11 = resultado_x10 % 11

# if resultado_x10_divido11 > 9:
#     resultado_x10_divido11 = 0
#     print(resultado_x10_divido11)
# else:
#     print(resultado_x10_divido11)



# # Validando o segundo digito

# cpf_2 = '746.824.890-70'                                                  # cpf = "777.777.77-77"                                            
# cpf_formatado_2 = ''
#                                                                         # Remove os pontos e o traço do CPF
# for num_cpf in cpf_2:                                                     # cpf_sem_pontos_e_traco = cpf.replace(".", "").replace("-", "")
#     if num_cpf.isdigit():                                           
#         cpf_formatado_2 += num_cpf

# print(cpf_formatado_2)                                                  # print(cpf_sem_pontos_e_traco)  # Output: 7777777777                                          

# cpf_formatado_sem_os_ultimos_dois_digitos_2 = cpf_formatado_2[:-1]
# num_multiplicador_cpf_2 = 11
# resultado_multiplicacao_cpf_2 = 0

# for i in cpf_formatado_sem_os_ultimos_dois_digitos_2:
#     i_int = int(i)
#     resultado_multiplicacao_cpf_2 += i_int * num_multiplicador_cpf_2
#     num_multiplicador_cpf_2 -= 1

# resultado_x10_2 = resultado_multiplicacao_cpf_2 * 10

# print(resultado_x10_2)

# resultado_x10_divido11_2 = resultado_x10_2 % 11

# if resultado_x10_divido11_2 > 9:
#     resultado_x10_divido11_2 = 0
#     print(resultado_x10_divido11_2)
# else:
#     print(resultado_x10_divido11_2)


# print(resultado_x10_divido11, resultado_x10_divido11_2)







### PROFESSOR

# cpf = '36440847007'  # Esse CPF gera o primeiro dígito como 10 (0)
cpf_enviado_usuario = '74682489070'
nove_digitos = cpf_enviado_usuario[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf_enviado_usuario} é válido')
else:
    print('CPF inválido')

