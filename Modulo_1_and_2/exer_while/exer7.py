"""
Escreva um programa que solicite ao usuário números inteiros. Pare a leitura quando o usuário 
digitar zero e, em seguida, imprima a soma de todos os números digitados.
"""

user_list = []
b = 0
while True:
     
    try:  
        user_action = int(input('Digite [0] para listar e somar ou [1] para continuar: '))

        if user_action == 0:  
            a = int(input('Digite um número: '))
            user_list.append(a)
            b += a
            print(user_list, b, sep='Soma: ')
        
    except Exception:
        print('Digite corretamente [0] ou [1]!')

#ChatGPT

# try:
#     numero = 1
#     soma = 0

#     print("Digite números inteiros (digite 0 para parar):")
#     while numero != 0:
#         numero = int(input())
#         soma += numero

#     print("A soma de todos os números digitados é:", soma)

# except ValueError:
#     print("Digite apenas números inteiros!")
