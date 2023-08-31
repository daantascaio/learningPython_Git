# Context Manager com classes - Criando e Usando gerenciadores de contexto
# Você pode implementar seus próprios protocolos
# apenas implementando os dunder methods que o
# Python vai usar.

# Isso é chamado de Duck typing. Um conceito
# relacionado com tipagem dinâmica onde o Python não
# está interessado no tipo, mas se alguns métodos existem
# no seu objeto para que ele funcione de forma adequada.

# Duck Typing:
# Quando vejo um pássaro que caminha como um pato, nada como
# um pato e grasna como um pato, eu chamo aquele pássaro de pato.

# Para criar um context manager, os métodos __enter__ e __exit__
# devem ser implementados.
# O método __exit__ receberá a classe de exceção, a exceção e o
# traceback. Se ele retornar True, exceção no with será
# suprimidas.
#
# Ex:
# with open('aula149.txt', 'w') as arquivo:
#     ...
from pathlib import Path

PATH_FILE = Path(__file__).parent / 'contextManager_class.txt'
# print(PATH_FILE)

class MyOpen:
    def __init__(self, path_file, modo):
        self.path_file = path_file
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        # return ' | o retorno do vai pra variável ---> "alguma_coisa"'
        print('ABRINDO ARQUIVO')
        self._arquivo = open(self.path_file,self.modo, encoding='utf8')
        return self._arquivo

    def __exit__(self, class_exception, exception_, traceback_):
        print('FECHANDO ARQUIVO')
        self._arquivo.close()
        

# instancia = MyContextManager(PATH_FILE, 'w')

with MyOpen(PATH_FILE, 'w') as file:
     file.write('Linha 1\n')
     file.write('Linha 2\n')
     file.write('Linha 3\n')
     file.write('Linha 4\n')
     file.write('Linha 5\n')
     print('WITH', file)

# with MyContextManager() as alguma_coisa:
#     print('WITH', alguma_coisa)