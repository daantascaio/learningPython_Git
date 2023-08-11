"""

Escreva um programa que verifique se um número fornecido pelo usuário é um número primo.

"""

# Claro! Vamos escrever um programa em Python que verifica se um número fornecido pelo usuário é um número primo utilizando o loop for para realizar a verificação.

try:
    numero = int(input("Digite um número inteiro positivo maior que 1: "))
    if numero <= 1:
        print("O número deve ser maior que 1.")
    else:
        eh_primo = True
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                eh_primo = False
                break

        if eh_primo:
            print(f"{numero} é um número primo.")
        else:
            print(f"{numero} NÃO é um número primo.")
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")


# Explicação:

#     O programa solicita ao usuário que digite um número inteiro positivo maior que 1 usando a função input(), e o valor digitado é armazenado na variável numero.
#     Em seguida, é feita uma verificação para garantir que o número fornecido seja maior que 1, pois, por definição, números primos são maiores que 1.
#     Utilizamos uma variável eh_primo para armazenar o resultado da verificação de primalidade do número.
#     Em seguida, utilizamos um loop for para iterar de 2 até a raiz quadrada do número (int(numero ** 0.5) + 1), verificando se há algum divisor além de 1 e o próprio número.
#     Caso seja encontrado um divisor, o número não é primo, e a variável eh_primo é definida como False. O loop é encerrado utilizando break.
#     Se ao final do loop, a variável eh_primo permanecer True, significa que o número é primo.
#     O programa imprime a mensagem adequada informando se o número é ou não primo.

# Dessa forma, o programa verificará se o número fornecido pelo usuário é primo ou não utilizando o loop for. 