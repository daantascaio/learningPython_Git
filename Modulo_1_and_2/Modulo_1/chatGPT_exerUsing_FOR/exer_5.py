"""

Escreva um programa que imprima a tabuada de multiplicação de um número fornecido pelo usuário.
O programa deve imprimir a tabuada de 1 a 10 para o número fornecido.

"""
# Eu
numero_do_usuario = input('Digite um número: ')
numero_multiplicador = 0
resultado_da_multiplicacao = 0

if numero_do_usuario.isdigit():
    numero_de_usuario_int = int(numero_do_usuario)

    print('A tabuada do seu número é: ')
    for numero_multiplicador in range(1, 11):
        
        resultado_da_multiplicacao = numero_de_usuario_int * numero_multiplicador
        print(resultado_da_multiplicacao)

else:
    print('Digite um número inteiro!')
    

######################## RESOLUÇÃO 1 (É UM PROGRAMA QUE NÃO TRATA ERROS) ######################## 

# ChatGPT
numero = int(input("Digite um número para ver a tabuada de multiplicação: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

#     Explicação:

#     Primeiro, solicitamos ao usuário que digite um número usando a função input. O valor é convertido para um inteiro usando int() e armazenado na variável numero.
#     O for percorre a sequência de números de 1 a 10 (novamente, o segundo parâmetro do range não está incluso).
#     Em cada iteração do loop, o resultado da multiplicação entre numero e i é calculado e armazenado na variável resultado.
#     Em seguida, usamos a função print() para exibir a tabuada da multiplicação para o número fornecido pelo usuário.

# Ao executar esse código, você será solicitado a digitar um número e, em seguida, verá a tabuada de multiplicação desse número, de 1 a 10, impressa na tela.



######################## RESOLUÇÃO 2 (USANDO try-except PARA TRATAR DADOS) ######################## 


# Se o usuário digitar uma letra ou qualquer outro valor inválido que não possa ser convertido para um número inteiro, ocorrerá um erro 
# durante a execução do programa. Para evitar esse problema, você pode incluir tratamento de exceção usando um bloco try-except para lidar com entradas inválidas.
# Vamos modificar a solução anterior para adicionar o tratamento de exceção:

# Solução do Exercício 5 com tratamento de exceção
try:
    numero = int(input("Digite um número para ver a tabuada de multiplicação: "))
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")

#     Explicação:

#     O bloco try envolve o código que pode gerar uma exceção (nesse caso, a conversão para inteiro).
#     Se o usuário digitar algo que não possa ser convertido para inteiro, uma exceção do tipo ValueError será lançada.
#     No bloco except, capturamos a exceção ValueError e exibimos uma mensagem amigável para o usuário, informando que a entrada é inválida.

# Com esse tratamento de exceção, o programa será capaz de lidar com entradas inválidas e evitará que ocorram erros não tratados durante a execução. 
# Em vez disso, ele exibirá uma mensagem apropriada para o usuário.



######################## RESOLUÇÃO 3 (USANDO if PARA TRATAR DADOS) ######################## 

# Sim, você pode usar um if para fazer o tratamento de entrada, e o uso do try-except também é uma abordagem válida e comumente utilizada para tratar exceções em Python.

# Usando o if para tratar a entrada:

# Solução do Exercício 5 com tratamento de exceção
try:
    numero = int(input("Digite um número para ver a tabuada de multiplicação: "))
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")


# Explicação:

#     Nessa abordagem, primeiro, lemos a entrada como uma string usando input e a armazenamos em numero_str.
#     Em seguida, utilizamos o método isdigit() para verificar se a string contém somente dígitos. 
#     Se for o caso, podemos converter a string para um número inteiro usando int() e prosseguir com o cálculo da tabuada e impressão na tela.
#     Se a entrada não for composta apenas de dígitos, o else é executado, e exibimos a mensagem informando que a entrada é inválida.

# Usando o try-except para tratar a entrada, como apresentado anteriormente, também é uma abordagem correta e, em alguns casos, pode ser mais concisa e legível.
# Essa abordagem é recomendada quando a exceção a ser tratada é específica, como no caso de ValueError quando ocorre uma falha na conversão de tipos. 
# Isso evita que exceções não tratadas interrompam abruptamente a execução do programa.

# Ambas as abordagens são aceitáveis, e você pode escolher a que melhor se adapta à sua preferência ou necessidade em cada situação. 
# O importante é garantir que o programa lide de forma adequada com entradas inválidas e forneça ao usuário um feedback adequado e compreensível.


