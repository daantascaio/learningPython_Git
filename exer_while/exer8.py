"""
Escreva um programa que simule um jogo de adivinhação. O programa deve gerar um número aleatório 
entre 1 e 100 e, em seguida, solicitar ao usuário para adivinhar o número. O programa deve informar 
se o palpite do usuário é muito alto, muito baixo ou correto. Continue solicitando palpites até que 
o usuário adivinhe corretamente.
"""

import random

# Gerar um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

# Loop para o jogo de adivinhação
while True:
    try:
        # Solicitar ao usuário para adivinhar o número
        palpite = int(input("Digite um número entre 1 e 100: "))

        # Verificar se o palpite é muito alto, muito baixo ou correto
        if palpite < numero_secreto:
            print("Palpite muito baixo. Tente novamente.")
        elif palpite > numero_secreto:
            print("Palpite muito alto. Tente novamente.")
        else:
            print("Parabéns! Você acertou o número.")
            break  # Sai do loop quando o palpite é correto

    except ValueError:
        print("Digite apenas números inteiros.")

"""
Explicação do código:

    O programa usa o módulo random para gerar um número aleatório entre 1 e 100, que é armazenado na variável numero_secreto.
    Em seguida, entra em um loop "while True" que continuará rodando até que o palpite do usuário seja correto e o comando break seja acionado.
    Dentro do loop, o programa solicita ao usuário que digite um número usando a função input, e o palpite é armazenado na variável palpite.
    O programa verifica se o palpite é menor que o numero_secreto, maior que o numero_secreto ou se é o palpite correto.
    Se o palpite for menor que o numero_secreto, o programa informa que o palpite é muito baixo e pede para o usuário tentar novamente.
    Se o palpite for maior que o numero_secreto, o programa informa que o palpite é muito alto e pede para o usuário tentar novamente.
    Se o palpite for igual ao numero_secreto, o programa informa que o palpite está correto, parabeniza o usuário e o loop é interrompido com o comando break.
    Se o usuário digitar algo que não é um número inteiro, o programa tratará o erro usando um bloco except para lidar com
    a exceção ValueError e informará que apenas números inteiros devem ser digitados.

Agora, o programa continuará solicitando ao usuário para adivinhar o número até que o palpite seja correto. 
Ele fornecerá feedback sobre os palpites do usuário (muito alto ou muito baixo) e, quando o palpite for correto, parabenizará o usuário.
"""