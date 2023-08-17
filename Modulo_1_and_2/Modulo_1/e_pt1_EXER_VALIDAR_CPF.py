"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

# soma dos 9 primeiros digitos
# multiplicar os 9 por uma contagem regressiva iniciando de 10
# o primeiro digito x10 o segundo digito x9 e assim em diante
# depois disso, somar o resultado deles
# multiplicar o resultado por 10
# dividir o resultado por 11 e pegar o resto
# se o resultado dessa conta for maior que 9, o digito do cpf deve ser 0
# se for um digito <9, o resultado é o o primeiro digito do cpf



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



################### MANEIRA QUE O PROFESSOR RESOLVEU O PROBLEMA ###################

cpf = '74682489070'
nove_digitos = cpf[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)



















