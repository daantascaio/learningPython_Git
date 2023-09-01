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




# Aqui está um exemplo simples de um contexto manager para trabalhar com arquivos:
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

# Uso do contexto manager
with FileManager('exemplo.txt', 'w') as file:
    file.write('Hello, world!')
# O arquivo é automaticamente fechado quando saímos do bloco 'with'

"""

Context managers em Python são usados para gerenciar recursos, como arquivos, conexões de rede, bancos de dados, sockets 
e outros objetos que precisam ser inicializados e liberados de forma adequada. Eles são particularmente úteis para garantir
que os recursos sejam liberados corretamente, mesmo em caso de exceções, e para manter o código mais limpo e legível.

O contexto manager é implementado em Python usando dois métodos especiais: __enter__() e __exit__(). Aqui está uma breve
explicação de como eles funcionam:

    __enter__(): Este método é chamado quando você entra no bloco de código que está dentro do contexto do gerenciador. 
    Ele é responsável por configurar o recurso e retornar qualquer objeto que você deseje usar dentro do bloco de contexto. 
    Por exemplo, ao trabalhar com arquivos, o método __enter__() geralmente abre o arquivo e retorna o objeto de arquivo.

    __exit__(): Este método é chamado quando você sai do bloco de código do contexto, seja de forma normal ou por meio de 
    uma exceção. Ele é responsável por liberar os recursos adequadamente, como fechar um arquivo ou encerrar uma conexão de
    banco de dados. Se ocorrer uma exceção no bloco de contexto, o método __exit__() pode manipulá-la, tomar medidas 
    apropriadas e decidir se a exceção deve ser propagada ou suprimida.

"""
###
"""

No exemplo acima, a classe FileManager atua como um contexto manager. Quando usamos o bloco with, o método __enter__() 
é chamado, abrindo o arquivo, e o objeto de arquivo é retornado e associado à variável file. Quando saímos do bloco 
with, o método __exit__() é chamado automaticamente, garantindo que o arquivo seja fechado, mesmo se ocorrer uma exceção.

Isso torna o código mais seguro e legível, evitando que você esqueça de fechar o arquivo manualmente ou lide com exceções 
de maneira incorreta. Context managers são amplamente usados em Python para recursos de gerenciamento, garantindo a limpeza 
e o gerenciamento adequado de recursos.

"""