"""
Escreva um programa que solicite ao usuário um número e imprima a contagem regressiva a partir 
desse número até zero.
"""

while True:
    num = input('Digite um número: ')

    try:
        num_int = int(num)
        break

    except ValueError:
        print('Digite um número inteiro!')


while num_int > 0:
    num_int -= 1
    print(num_int, end= ' - ')



#ChatGPT

# Solicita ao usuário um número inteiro
# numero = int(input("Digite um número inteiro: "))

# # Garante que o número seja positivo
# if numero < 0:
#     print("Por favor, digite um número inteiro positivo.")
# else:
#     # Enquanto o número for maior ou igual a zero, imprime-o e decrementa o valor em 1
#     while numero >= 0:
#         print(numero)
#         numero -= 1

# O programa solicitará ao usuário um número inteiro. Se o número for negativo, o programa informará
# que é necessário digitar um número inteiro positivo. Caso contrário, o programa imprimirá a contagem 
# regressiva a partir do número fornecido até zero, imprimindo cada número em uma linha separada no console. 
# O loop "while" continuará executando até que o valor do número seja menor do que zero, momento em que o loop será encerrado.




