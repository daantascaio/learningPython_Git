nome_sobrenome = 'Caio Dantas'
altura = 1.83
peso = 105
imc = peso / (altura ** 2)

# print(nome_sobrenome, 'tem', altura, 'de altura, e pesa', peso, 'quilos e seu IMC é:', imc)


#Introdução à formatação de STRINGS (str)

formatando_a_string = f'{nome_sobrenome} tem {altura:.2f} de altura e pesa {peso} quilos, seu IMC é: {imc:.2f}'
print(formatando_a_string)

