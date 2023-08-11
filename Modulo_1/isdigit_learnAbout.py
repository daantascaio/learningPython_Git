"""
O método isdigit() é uma função pertencente a objetos do tipo string em várias
linguagens de programação, incluindo Python. Essa função é usada para verificar
se todos os caracteres em uma string são dígitos numéricos.

Em Python, o método isdigit() retorna True se todos os caracteres da string
forem dígitos numéricos (0 a 9) e a string não estiver vazia. Caso contrário,
retorna False. Veja um exemplo de uso em Python:
"""

texto1 = "12345"
texto2 = "42a7"  # contém um caractere não numérico (a)
texto3 = ""      # string vazia

print(texto1.isdigit())  # Saída: True
print(texto2.isdigit())  # Saída: False
print(texto3.isdigit())  # Saída: False

"""
Nesse exemplo, texto1.isdigit() retorna True porque todos os caracteres da string 
texto1 são dígitos. texto2.isdigit() retorna False porque há o caractere 'a', que 
não é um dígito numérico, e texto3.isdigit() também retorna False porque a string 
está vazia, não contendo nenhum dígito.

O método isdigit() é útil para validar se uma string representa um número inteiro 
positivo, antes de realizar operações numéricas com ela, por exemplo.
"""