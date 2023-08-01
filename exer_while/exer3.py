"""
Escreva um programa que calcule a soma de todos os números inteiros de 1 a N, onde N é um número 
inteiro fornecido pelo usuário.
"""

while True:

    num_user = input('Digite um número: ')
    try:

        num_user_int = int(num_user)
        break

    except ValueError:
        print('Digite um número inteiro!')


contador = 0
soma = 0

while num_user_int > 0:
    
    num_user_int -= 1
    soma += 1
    contador += soma
    
print(contador)


#ChatGPT
try:
    N = int(input("Digite um número inteiro N: "))
    
    # Garante que N seja um número positivo
    if N < 0:
        print("Por favor, digite um número inteiro positivo.")
    else:
        soma = 0
        num = 1

        while num <= N:
            soma += num
            num += 1

        print(f"A soma de todos os números inteiros de 1 a {N} é: {soma}")

except ValueError:
    print("Digite apenas números!")

"""
Explicação do código:

    O programa solicita ao usuário um número inteiro N usando a função input.
    Em seguida, é feita uma verificação para garantir que N seja um número positivo. Se N for negativo, o programa exibirá uma mensagem de erro.
    Caso contrário, o programa inicializa duas variáveis: soma, que será usada para armazenar a soma dos números, e num, que começa com o valor 1.
    O programa entra em um loop "while", que continuará executando enquanto num for menor ou igual a N.
    Dentro do loop, o programa adiciona o valor de num à variável soma e, em seguida, incrementa num em 1.
    Quando o valor de num for maior que N, o loop termina.
    Finalmente, o programa imprime a soma de todos os números inteiros de 1 a N.

Agora, o programa solicitará ao usuário um número inteiro N e calculará a soma de todos os números inteiros de 1 a N. 
Se o usuário digitar um valor inválido (não inteiro), o programa informará sobre o erro.
"""
