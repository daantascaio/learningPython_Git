"""
Escreva um programa que solicite ao usuário que digite uma senha.
Continue solicitando a senha até que o usuário digite a senha correta.
Quando a senha correta for digitada, imprima uma mensagem de boas-vindas.
"""
import os


senha_correta = 'senhacorreta123@'
senha_user = input('Digite sua senha: ')


while senha_user != senha_correta:
    os.system('cls')
    print(f'Senha incorreta! \nDigite novamente.')

    senha_user = input('Digite sua senha: ')


os.system('cls')
print('Bem Vindo!')

#ChatGPT

# Definindo a senha correta
# senha_correta = "senha123"

# while True:
#     # Solicita ao usuário que digite a senha
#     senha_digitada = input("Digite a senha: ")

#     # Verifica se a senha está correta
#     if senha_digitada == senha_correta:
#         print("Bem-vindo(a)!")
#         break  # Sai do loop quando a senha correta é digitada
#     else:
#         print("Senha incorreta. Tente novamente.")

"""
Explicação do código:

    O programa entra em um loop "while True", que continuará executando até que a senha correta seja digitada e o comando break seja acionado.
    Dentro do loop, o programa solicita ao usuário que digite a senha usando a função input.
    Em seguida, verifica se a senha digitada é igual à senha correta definida na variável senha_correta.
    Se a senha estiver correta, o programa imprime uma mensagem de boas-vindas e sai do loop usando o comando break.
    Caso contrário, se a senha estiver incorreta, o programa imprime uma mensagem de erro e o loop continua, pedindo ao usuário que digite a senha novamente.

Agora, o programa continuará solicitando a senha ao usuário até que a senha correta seja digitada. 
Quando isso acontecer, ele imprimirá uma mensagem de boas-vindas e encerrará a execução.
"""
    