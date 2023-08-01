"""
Escreva um programa que gere a sequência de Fibonacci até o N-ésimo termo, onde N é um número 
inteiro fornecido pelo usuário. A sequência de Fibonacci é uma sequência de números em que cada 
número é a soma dos dois anteriores (começando por 0 e 1).
"""
# exibir os números cuja divisão resulta no resto 1,6

try:
    N = int(input("Digite um número inteiro N para a sequência de Fibonacci: "))

    # Verificação para garantir que N seja um número positivo
    if N < 1:
        print("Por favor, digite um número inteiro positivo maior ou igual a 1.")
    else:
        # Inicializando os primeiros dois termos da sequência
        termo_anterior = 0
        termo_atual = 1

        # Imprimir os primeiros N termos da sequência
        print("Sequência de Fibonacci:")
        count = 0
        while count < N:
            print(termo_anterior, end=" ")

            # Calcular o próximo termo e atualizar os valores dos termos anteriores
            proximo_termo = termo_anterior + termo_atual
            termo_anterior = termo_atual
            termo_atual = proximo_termo

            count += 1

except ValueError:
    print("Digite apenas números!")

"""
Explicação do código:

    O código usa um loop while para gerar os primeiros N termos da sequência de Fibonacci.
    A variável count é inicializada com zero antes do loop começar.
    O loop while continuará executando até que count seja igual a N.
    Dentro do loop, o programa imprime o valor do termo_anterior, que é o termo atual da sequência.
    O próximo termo é calculado somando o termo_anterior e o termo_atual, e os valores dos termos são atualizados para avançar na sequência.
    O contador count é incrementado em 1 a cada iteração do loop para acompanhar quantos termos já foram impressos.

Agora, o programa solicitará ao usuário um número inteiro N e imprimirá os primeiros N termos da sequência de Fibonacci usando um loop "while". 
Se o usuário digitar um valor inválido (não inteiro), o programa informará sobre o erro.
"""


    

    