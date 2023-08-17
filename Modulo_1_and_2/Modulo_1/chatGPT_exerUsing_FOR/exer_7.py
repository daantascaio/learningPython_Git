"""

Escreva um programa que imprima a seguinte sequência: 1, 3, 6, 10, 15, 21, ...

"""

# Não entendi

# Claro! Vamos resolver o Exercício 7, que consiste em escrever um programa que imprima a seguinte sequência: 1, 3, 6, 10, 15, 21, ...

# Essa sequência segue um padrão em que cada número é a soma dos números naturais consecutivos a partir de 1. Por exemplo:

# 1 = 1
# 3 = 1 + 2
# 6 = 1 + 2 + 3
# 10 = 1 + 2 + 3 + 4
# 15 = 1 + 2 + 3 + 4 + 5
# 21 = 1 + 2 + 3 + 4 + 5 + 6
# ...

# Vamos implementar o código para gerar essa sequência:

def sequencia_soma_naturais(n):
    sequencia = []
    soma = 0

    for i in range(1, n + 1):
        soma += i
        sequencia.append(soma)

    return sequencia

try:
    N = int(input("Digite a quantidade de elementos da sequência: "))
    resultado = sequencia_soma_naturais(N)
    print(resultado)
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")


# Explicação:

#     A função sequencia_soma_naturais(n) recebe um número inteiro n como entrada e retorna uma lista contendo os primeiros n elementos da sequência.
#     Inicializamos uma lista vazia chamada sequencia para armazenar os números da sequência e a variável soma para calcular a soma dos números.
#     Utilizamos um loop for para iterar de 1 até n + 1, pois queremos que a sequência tenha n elementos.
#     Em cada iteração, adicionamos o valor atual do índice i à variável soma, calculando a soma dos números naturais consecutivos.
#     Em seguida, adicionamos o valor da soma à lista sequencia.
#     Após o loop, a função retorna a lista sequencia com os elementos da sequência calculada.

# No bloco principal do programa, solicitamos ao usuário a quantidade de elementos da sequência (N) e chamamos a função sequencia_soma_naturais(N) para gerar a sequência. O resultado é então impresso na tela.

# Espero que isso tenha sido útil! Se tiver mais perguntas ou precisar de mais esclarecimentos, sinta-se à vontade para perguntar! Estou aqui para ajudar.


# RESOLUÇÃO 2


# Claro! Se você deseja resolver o Exercício 7 sem usar uma função, podemos fazer 
# isso diretamente no bloco principal do programa usando apenas um loop for:

try:
    N = int(input("Digite a quantidade de elementos da sequência: "))
    soma = 0

    for i in range(1, N + 1):
        soma += i
        print(soma)

except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")


# Explicação:

#     O programa solicita ao usuário a quantidade de elementos da sequência (N) por meio da função input e converte o valor inserido para um número inteiro usando int().
#     Em seguida, utilizamos um loop for para iterar de 1 até N + 1, pois queremos que a sequência tenha N elementos.
#     Em cada iteração, adicionamos o valor atual do índice i à variável soma, calculando a soma dos números naturais consecutivos.
#     Imprimimos o valor da soma na tela a cada iteração, mostrando a sequência resultante.

# Essa solução imprime a sequência diretamente no bloco principal do programa, sem a necessidade de criar uma função específica para isso.

# Se tiver mais perguntas ou precisar de mais esclarecimentos, sinta-se à vontade para perguntar! Estou aqui para ajudar.