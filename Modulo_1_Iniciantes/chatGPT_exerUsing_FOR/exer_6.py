"""

Escreva um programa que imprima os primeiros N números primos, onde N é fornecido pelo usuário.

"""
# Não consegui resolver 


# ChatGPT
# Sem usar a função is.primo
try:
    N = int(input("Digite a quantidade de números primos que deseja encontrar: "))
    contador = 0
    numero = 2

    while contador < N:
        eh_primo = True
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                eh_primo = False
                break
        
        if eh_primo:
            print(numero)
            contador += 1

        numero += 1

except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")

#     Explicação:

#     O programa solicita ao usuário a quantidade de números primos que ele deseja encontrar (N).
#     Utilizamos um loop while para encontrar os N números primos.
#     Para verificar se um número é primo, utilizamos um loop for que percorre todos os valores de 2 até a raiz quadrada do número atual (int(numero ** 0.5) + 1).
#     Se o número atual for divisível por algum valor dentro do intervalo, sabemos que ele não é primo e definimos a variável eh_primo como False.
#     Caso o número não seja divisível por nenhum valor dentro do intervalo, a variável eh_primo permanecerá True, indicando que o número é primo.
#     Se a variável eh_primo for True, significa que encontramos um número primo, então imprimimos esse número e incrementamos o contador.
#     Continuamos verificando os próximos números até encontrarmos N números primos.

# Essa solução usa apenas loops while e for para encontrar os N primeiros números primos. Se tiver mais dúvidas ou precisar de mais esclarecimentos, sinta-se à vontade para perguntar!




# Usando a função is.primo

def is_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

try:
    N = int(input("Digite a quantidade de números primos que deseja encontrar: "))
    contador = 0
    numero = 2

    while contador < N:
        if is_primo(numero):
            print(numero)
            contador += 1
        numero += 1
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")


# Explicação:

#     Definimos uma função is_primo(numero) que verifica se um número é primo ou não. Essa função é usada para determinar se um valor é primo dentro do loop.
#     O bloco try é utilizado para tratar possíveis erros de conversão de tipos, caso o usuário insira um valor inválido para N.
#     Dentro do bloco try, lemos o valor de N do usuário e iniciamos as variáveis contador e numero.
#     O loop while continua até encontrarmos N números primos. Em cada iteração do loop, verificamos se o valor atual de numero é primo usando a função is_primo().
#     Se numero for primo, ele é impresso na tela, e o contador é incrementado.
#     O valor de numero é incrementado em 1 a cada iteração, permitindo que verifiquemos os próximos números em ordem crescente.

# Essa solução utiliza a função is_primo() para determinar se um número é primo ou não, e o programa encontra e exibe os primeiros N números primos, conforme solicitado no exercício.