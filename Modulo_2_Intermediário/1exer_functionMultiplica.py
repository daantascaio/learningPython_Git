# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplica(*args):
    resultado = 1
    for i in args:
        resultado *= i
    return resultado

print(multiplica(1, 2, 3, 4, 5))

# Crie uma função que fala se um número é impar ou é par
# Retorne se o número é par ou ímpar

def par_impar(numero):
    num1 = int(input(numero))

    if num1 % 2 == 0:
        valida = True
    else:
        valida = False

    return valida

numero = par_impar('Digite um número: ')

print(par_impar(numero))


#PROFESSOR
def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


multiplicação = multiplicar(10, 2, 3, 4, 5)
print(multiplicação)


# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.
def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar'


outro_par_impar = par_impar
dois_e_par = outro_par_impar(2)
print(dois_e_par)
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))

print(par_impar is outro_par_impar)