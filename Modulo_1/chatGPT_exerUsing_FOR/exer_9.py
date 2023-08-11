"""

Escreva um programa que receba uma lista de números do usuário e calcule a média dos valores.

"""

# Claro! Vamos escrever um programa em Python que recebe uma lista de números do usuário e calcula a média dos valores inseridos. 
# Utilizaremos um loop para solicitar os números e, em seguida, calcularemos a média após a entrada dos valores.

# Solicita ao usuário a lista de números, separados por espaço
numeros_str = input("Digite a lista de números separados por espaço: ")

# Converte a lista de números em uma lista de inteiros
numeros = [int(num) for num in numeros_str.split()]

# Calcula a média dos valores
media = sum(numeros) / len(numeros)

# Imprime a média
print(f"A média dos valores é: {media}")


# Explicação:

#     O programa solicita ao usuário que digite uma lista de números separados por espaço, usando a função input(). Os números digitados pelo usuário são armazenados na variável numeros_str.
#     Em seguida, utilizamos a função split() para separar os números e criar uma lista de strings. Essa lista de strings é convertida em uma lista de inteiros usando a compreensão de lista ([int(num) for num in numeros_str.split()]), e os números resultantes são armazenados na lista numeros.
#     Calculamos a média dos valores na lista numeros somando todos os valores com sum(numeros) e dividindo pela quantidade de números na lista, que é obtida com len(numeros).
#     Por fim, imprimimos a média dos valores usando a função print().

# Com este programa, você pode inserir uma lista de números e obter a média dos valores digitados. Se tiver alguma dúvida ou precisar de mais esclarecimentos, sinta-se à vontade para perguntar! Estou aqui para ajudar.



# Resolução 2

# Claro! Vamos reescrever o programa utilizando o loop for para receber a lista de números do usuário:

# Solicita ao usuário a quantidade de números na lista
n = int(input("Digite a quantidade de números na lista: "))

# Inicializa uma lista vazia para armazenar os números
numeros = []

# Loop para receber os números do usuário
for i in range(n):
    numero = int(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)

# Calcula a média dos valores
media = sum(numeros) / len(numeros)

# Imprime a média
print(f"A média dos valores é: {media}")


# Explicação:

#     O programa começa solicitando ao usuário a quantidade de números que ele deseja inserir na lista, armazenando esse valor na variável n.
#     Inicializamos uma lista vazia chamada numeros para armazenar os números informados pelo usuário.
#     Utilizamos um loop for para iterar n vezes, conforme a quantidade de números que o usuário deseja inserir na lista.
#     Dentro do loop, solicitamos ao usuário para digitar o número na posição atual (i + 1), convertendo o valor inserido em um inteiro, e o adicionamos à lista numeros usando o método append().
#     Após o loop, calculamos a média dos valores na lista numeros somando todos os valores com sum(numeros) e dividindo pela quantidade de números na lista, que é obtida com len(numeros).
#     Por fim, imprimimos a média dos valores usando a função print().

# Essa versão com o loop for realiza a mesma tarefa que a versão anterior, permitindo que o usuário insira uma lista de números e calculando a média dos valores digitados. 
# Se tiver mais perguntas ou precisar de mais esclarecimentos, sinta-se à vontade para perguntar! Estou aqui para ajudar.